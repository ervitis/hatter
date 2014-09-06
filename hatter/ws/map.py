# coding=utf-8

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse

from hatter import models

import json


@ensure_csrf_cookie
def get_actuaciones(request):
    """
    Get all actuaciones
    :param request:
    :return: json
    """

    actuaciones = models.Actuacion.objects.all()

    dict_actuaciones = []
    for actuacion in actuaciones:
        if actuacion.latitud:
            dict_actuacion = {
                'nombre':   actuacion.nombre,
                'lat':      actuacion.latitud,
                'lon':      actuacion.longitud
            }
        elif actuacion.emplazamiento:
            dict_actuacion = {
                'nombre':   actuacion.nombre,
                'lat':      actuacion.emplazamiento.latitud,
                'lon':      actuacion.emplazamiento.longitud
            }
        else:
            dict_actuacion = {
                'nombre':   actuacion.nombre,
                'address':  actuacion.direccion + ', ' + actuacion.codigo_postal + ', ' + actuacion.provincia.nombre
            }

        dict_actuaciones.append(dict_actuacion)

    return HttpResponse(json.dumps(dict_actuaciones), content_type='application/json')