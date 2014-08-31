# coding=utf-8

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
from django.db.models import Q

from hatter import models

import json

@ensure_csrf_cookie
def search_agenda_tecnico(request):
    jsonTecnicos = []

    if request.method == 'POST':
        dni = request.POST.get('sDni')
        nombre = request.POST.get('sName')

        results = models.Tecnico.objects.select_related('agenda__evento').filter(
            Q(evento__isnull=True) | Q(evento__tecnico__nombre__contains=nombre) | Q(evento__tecnico__dni__contains=dni))

        for result in results:
            jsonEvento = []
            jsonAgenda = []

            for evento in result.evento.all():
                jsonEvento = {
                    'evento_id':        evento.id
                }

            for agenda in result.agenda.all():
                jsonAgenda = {
                    'agenda_id':        agenda.id
                }

            jsonTecnico = {
                'tecnico_id':       result.id,
                'tecnico_nom_ape':  result.nombre + ' ' + result.apellidos,
                'tecnico_dni':      result.dni,
                'eventos':          jsonEvento,
                'agenda':           jsonAgenda
            }
            jsonTecnicos.append(jsonTecnico)

    return HttpResponse(json.dumps(jsonTecnicos))
