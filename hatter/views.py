# coding=utf-8

from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist

from functions.log import check_user
from functions.horario import parse_spain_format_to_sql, date_range

from hatter import models, forms


class IndexView(TemplateView):
    """
    Index
    """

    @method_decorator(check_user)
    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)


class ActuacionesView(ListView):
    """
    Get the list of tasks
    """

    context_object_name = 'listado_actuaciones'
    paginate_by = 3
    queryset = models.Actuacion.objects.select_related('actuacion__tecnico__evento').order_by('-id')

    @method_decorator(check_user)
    def dispatch(self, request, *args, **kwargs):
        return super(ActuacionesView, self).dispatch(request, *args, **kwargs)


def actuaciones_new_view(request):
    """
    For the view new actuacion
    :param request:
    :return: post redirect to listado_actuaciones or create one
    """

    if request.method == 'POST':
        form_actuacion = forms.ActuacionForm(request.POST, instance=models.Actuacion())
        form_detalle_actuacion = forms.DetalleActuacionForm(
            request.POST, instance=models.DetalleActuacion()
        )

        if form_actuacion.is_valid() and form_detalle_actuacion.is_valid():
            actuacion = form_actuacion.save()
            detalle_actuacion = form_detalle_actuacion.save(commit=False)
            detalle_actuacion.actuacion = actuacion
            detalle_actuacion.utc = '+0200'
            detalle_actuacion.save()

            return redirect('listado_actuaciones')
    else:
        form_actuacion = forms.ActuacionForm(instance=models.Actuacion())
        form_detalle_actuacion = forms.DetalleActuacionForm(instance=models.DetalleActuacion())

    return render_to_response('layout/actuaciones/crear.html', {
        'form_actuacion':           form_actuacion,
        'form_detalle_actuacion':   form_detalle_actuacion,
        'urlaction':                'new_actuacion',
    }, context_instance=RequestContext(request))


def actuaciones_update_view(request, actuacion_id):
    """
    Update an actuacion
    :param request:
    :param actuacion_id: the id of the actuacion
    :return: post redirect to listado_actuacion or update one
    """

    if request.method == 'POST':
        form_actuacion = forms.ActuacionForm(
            request.POST, instance=get_object_or_404(models.Actuacion, pk=actuacion_id)
        )
        form_detalle_actuacion = ''

        try:
            form_detalle_actuacion = forms.DetalleActuacionForm(
                request.POST, instance=models.DetalleActuacion.objects.get(actuacion=actuacion_id)
            )
        except ObjectDoesNotExist:
            form_detalle_actuacion = forms.DetalleActuacionForm(
                request.POST, instance=models.DetalleActuacion()
            )

        if form_actuacion.is_valid() and form_detalle_actuacion.is_valid():
            actuacion = form_actuacion.save()
            detalle_actuacion = form_detalle_actuacion.save(commit=False)
            detalle_actuacion.actuacion = actuacion
            detalle_actuacion.utc = '+0200'
            detalle_actuacion.save()

            return redirect('listado_actuaciones')
    else:
        form_actuacion = forms.ActuacionForm(instance=get_object_or_404(models.Actuacion, pk=actuacion_id))
        form_detalle_actuacion = ''

        try:
            models.DetalleActuacion.objects.get(actuacion=actuacion_id)
            form_detalle_actuacion = forms.DetalleActuacionForm(
                instance=models.DetalleActuacion.objects.get(actuacion=actuacion_id)
            )
        except ObjectDoesNotExist:
            form_detalle_actuacion = forms.DetalleActuacionForm(instance=models.DetalleActuacion())

    return render_to_response('layout/actuaciones/actualizar.html', {
        'form_actuacion':           form_actuacion,
        'form_detalle_actuacion':   form_detalle_actuacion,
        'urlaction':                'update_actuacion',
        'id':                       actuacion_id,
    }, context_instance=RequestContext(request))


class MapaView(TemplateView):
    """
    MapaView template
    """

    template_name = 'layout/mapa/mapa.html'


class TecnicosView(ListView):
    """
    TecnicosView list
    """

    template_name = 'layout/tecnicos/listado.html'
    context_object_name = 'listado_tecnicos'
    paginate_by = 20
    queryset = models.Tecnico.objects.order_by('id')


class TecnicosNewView(CreateView):
    """
    Create new tecnico
    """

    template_name = 'layout/tecnicos/crear.html'
    models = models.Tecnico
    form_class = forms.TecnicoForm

    def form_invalid(self, form):
        return super(TecnicosNewView, self).form_invalid(form)

    def form_valid(self, form):
        tecnico = models.Tecnico()

        tecnico.nombre = form.cleaned_data['nombre']
        tecnico.apellidos = form.cleaned_data['apellidos']
        tecnico.dni = form.cleaned_data['dni']

        tecnico.save()

        return redirect('listado_tecnicos')


class TecnicosUpdateView(UpdateView):
    """
    Update tecnico
    """

    template_name = 'layout/tecnicos/actualizar.html'
    form_class = forms.TecnicoForm
    model = models.Tecnico

    def form_valid(self, form):
        self.object.save()

        return redirect('listado_tecnicos')

    def form_invalid(self, form):
        return super(TecnicosUpdateView, self).form_invalid(form)


class ToolsView(TemplateView):
    """
    Tools template
    """

    template_name = 'layout/tools/tools.html'


def listado_tecnicos(request):
    if request.method == 'POST':
        nombre = request.POST.get('turnoNombre')
        dni = request.POST.get('turnoDni')

        tecnico = models.Tecnico()
        tecnicos = tecnico.get_tecnicos_by_nombre_dni(nombre=nombre, dni=dni)

        turnos = forms.TurnoForm()

        return render_to_response('layout/tools/tools.html', {
            'tecnicos': tecnicos,
            'turnos':   turnos,
        }, context_instance=RequestContext(request))


def save_turnos(request):
    if request.method == 'POST':
        listas = request.POST

        dict_listas = dict(listas)
        if 'turno_check' in dict_listas:
            for v in range(0, len(dict_listas['turno_check'])):
                tecnico = models.Tecnico.objects.get(pk=dict_listas['hidden_tec'][v])

                turno_escogido = dict_listas['turnos'][v];
                fecha_ini_escogida = dict_listas['fecha_inicio'][v]
                fecha_fin_escogida = dict_listas['fecha_fin'][v]

                if '' == turno_escogido or '' == fecha_ini_escogida or '' == fecha_fin_escogida:
                    return render_to_response('layout/tools/tools.html', {
                        'executed': True,
                        'success': False,
                    }, context_instance=RequestContext(request))

                turno = models.Turno.objects.get(pk=turno_escogido)
                fecha_inicio = parse_spain_format_to_sql(fecha_ini_escogida)
                fecha_fin = parse_spain_format_to_sql(fecha_fin_escogida)

                for fecha in date_range(start=fecha_inicio, end=fecha_fin):
                    try:
                        agenda = models.Agenda.objects.get(fecha=fecha, tecnico=tecnico.pk)

                        # Update
                        agenda.turno = turno
                        agenda.fecha = fecha
                        agenda.save()

                    except ObjectDoesNotExist:
                        # Create
                        ag = models.Agenda()
                        ag.fecha = fecha
                        ag.tecnico = tecnico
                        ag.turno = turno
                        ag.save()

            return render_to_response('layout/tools/tools.html', {
                'executed': True,
                'success': True,
            }, context_instance=RequestContext(request))

        return render_to_response('layout/tools/tools.html', {
            'executed': True,
            'success': False,
        }, context_instance=RequestContext(request))
