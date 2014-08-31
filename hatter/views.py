# coding=utf-8

from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator

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


class ActuacionesNewView(CreateView):
    template_name = 'layout/actuaciones/crear.html'
    form_class = forms.ActuacionForm
    models = models.Actuacion

    def form_invalid(self, form):
        return super(ActuacionesNewView, self).form_invalid(form)

    def form_valid(self, form):
        actuacion = models.Actuacion()

        actuacion.nombre = form.cleaned_data['nombre']
        actuacion.alerta = form.cleaned_data['alerta']
        actuacion.cliente = form.cleaned_data['cliente']
        actuacion.codigo_postal = form.cleaned_data['codigo_postal']
        actuacion.direccion = form.cleaned_data['direccion']
        actuacion.emplazamiento = form.cleaned_data['emplazamiento']
        actuacion.estado = form.cleaned_data['estado']
        actuacion.latitud = form.cleaned_data['latitud']
        actuacion.longitud = form.cleaned_data['longitud']
        actuacion.prioridad = form.cleaned_data['prioridad']
        actuacion.severidad = form.cleaned_data['severidad']
        actuacion.provincia = form.cleaned_data['provincia']
        actuacion.tipo_via = form.cleaned_data['tipo_via']

        actuacion.save()

        return redirect('listado_actuaciones')


class ActuacionesUpdateView(UpdateView):
    template_name = 'layout/actuaciones/actualizar.html'
    form_class = forms.ActuacionForm
    model = models.Actuacion

    def form_valid(self, form):
        self.object.save()

        return redirect('listado_actuaciones')

    def form_invalid(self, form):
        return super(ActuacionesUpdateView, self).form_invalid(form)


class MapaView(TemplateView):
    template_name = 'layout/mapa/mapa.html'


class TecnicosView(ListView):
    template_name = 'layout/tecnicos/listado.html'
    context_object_name = 'listado_tecnicos'
    paginate_by = 20
    queryset = models.Tecnico.objects.order_by('id')


class TecnicosNewView(CreateView):
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
    template_name = 'layout/tecnicos/actualizar.html'
    form_class = forms.TecnicoForm
    model = models.Tecnico

    def form_valid(self, form):
        self.object.save()

        return redirect('listado_tecnicos')

    def form_invalid(self, form):
        return super(TecnicosUpdateView, self).form_invalid(form)
