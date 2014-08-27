# coding=utf-8

from django.shortcuts import redirect
from django.views import generic

from hatter import models, forms

import logging


class IndexView(generic.TemplateView):
    """
    Index
    """

    template_name = 'index.html'


class ActuacionesView(generic.ListView):
    """
    Get the list of tasks
    """

    template_name = 'layout/actuaciones/listado.html'
    context_object_name = 'listado_actuaciones'
    paginate_by = 10
    queryset = models.Actuacion.objects.order_by('id')


class ActuacionesFormView(generic.FormView):
    template_name = 'layout/actuaciones/crear.html'
    form_class = forms.ActuacionForm

    def form_invalid(self, form):
        return super(ActuacionesFormView, self).form_invalid(form)

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
