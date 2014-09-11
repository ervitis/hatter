# coding=utf-8

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse

from hatter import models

import json
from datetime import datetime, time


@ensure_csrf_cookie
def search_agenda_tecnico(request):
    """
    Get tecnicos and filter them
    :param request:
    :return: json
    """

    json_tecnicos = []

    if request.is_ajax() and request.method == 'POST':
        dni = request.POST.get('sDni')
        nombre = request.POST.get('sName')

        tecnico = models.Tecnico()

        result_eventos = tecnico.get_eventos_by_tecnico_data(nombre=nombre, dni=dni)

        for result in result_eventos:
            json_evento = {
                'tecnico_id':       result['id'],
                'tecnico_nom_ape':  result['nombre'] + ' ' + result['apellidos'],
                'actuacion_id':     result['evento__id'],
                'estado_id':        result['evento__estado__id'],
                'hora_inicio':      datetime.strftime(result['evento__detalleactuacion__fecha_inicio'], '%H:%M'),

            }

            if result['evento__detalleactuacion__fecha_fin']:
                json_evento['hora_fin'] = datetime.strftime(result['evento__detalleactuacion__fecha_fin'], '%H:%M')

            json_tecnicos.append(json_evento)

    return HttpResponse(json.dumps(json_tecnicos), content_type='application/json')


@ensure_csrf_cookie
def search_turnos_tecnico(request):
    """
    Get the schedule of a technician
    :param request:
    :return: json_tecnico
    """

    json_agendas = []

    if request.is_ajax() and request.method == 'POST':
        dni = request.POST.get('sDni')
        nombre = request.POST.get('sName')
        fecha = datetime.now()
        fecha = '%s-%s-%s' % (fecha.year, fecha.month, fecha.day)

        agenda = models.Agenda()

        result_agenda = agenda.get_turnos_by_tecnico(nombre=nombre, dni=dni, fecha=fecha)

        json_agendas = []

        for result in result_agenda:
            json_agenda = {
                'tecnico_id':   result['id'],
                'turno_inicio': time.strftime(result['turno__hora_inicio'], '%H:%M'),
                'turno_fin':    time.strftime(result['turno__hora_fin'], '%H:%M')
            }

            json_agendas.append(json_agenda)

    return HttpResponse(json.dumps(json_agendas), content_type='application/json')
