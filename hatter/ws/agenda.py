# coding=utf-8

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
from django.db.models import Q

from hatter import models

import json


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

        results = models.Tecnico.objects.select_related('agenda__evento__actuacion__detalle_actuacion').filter(
            Q(evento__isnull=True) | Q(evento__tecnico__nombre__contains=nombre) | Q(evento__tecnico__dni__contains=dni)
        )[:5]

        for result in results:
            json_evento = []
            json_agenda = []

            for evento in result.evento.all():
                json_evento = {
                    'evento_id':        evento.id
                }

            for agenda in result.agenda.all():
                json_agenda = {
                    'agenda_id':        agenda.id
                }

            json_tecnico = {
                'tecnico_id':       result.id,
                'tecnico_nom_ape':  result.nombre + ' ' + result.apellidos,
                'eventos':          json_evento,
                'agenda':           json_agenda
            }
            json_tecnicos.append(json_tecnico)

    return HttpResponse(json.dumps(json_tecnicos), content_type='application/json')
