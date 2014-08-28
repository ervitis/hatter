# coding=utf-8

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.views.decorators.csrf import ensure_csrf_cookie

from hatter import models, forms

import logging
import json


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
    paginate_by = 3
    queryset = models.Actuacion.objects.order_by('-id')


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


class MapaView(generic.TemplateView):
    template_name = 'layout/mapa/mapa.html'


@ensure_csrf_cookie
def get_actuaciones(request):
    actuaciones = models.Actuacion.objects.all()

    dict_actuaciones = []
    for actuacion in actuaciones:
        if actuacion.latitud:
            dict_actuacion = {
                'lat': actuacion.latitud,
                'lon': actuacion.longitud
            }
        elif actuacion.emplazamiento:
            dict_actuacion = {
                'lat': actuacion.emplazamiento.latitud,
                'lon': actuacion.emplazamiento.longitud
            }
        else:
            dict_actuacion = {
                'address': actuacion.direccion + ', ' + actuacion.codigo_postal + ', ' + actuacion.provincia.nombre
            }

        dict_actuaciones.append(dict_actuacion)

    return HttpResponse(json.dumps(dict_actuaciones), content_type='application/json')