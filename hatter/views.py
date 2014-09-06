# coding=utf-8

from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.template import RequestContext

from functions.log import check_user

from hatter import models, forms

import logging


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
    queryset = models.Actuacion.objects.order_by('-id')

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
            request.POST, instance=models.DetalleActuacion(), prefix='detalle'
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
        form_detalle_actuacion = forms.DetalleActuacionForm(instance=models.DetalleActuacion(), prefix='detalle')

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
        form_detalle_actuacion = forms.DetalleActuacionForm(
            request.POST, instance=models.DetalleActuacion.objects.get(actuacion=actuacion_id)
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
        form_detalle_actuacion = forms.DetalleActuacionForm(
            instance=models.DetalleActuacion.objects.get(actuacion=actuacion_id)
        )

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
