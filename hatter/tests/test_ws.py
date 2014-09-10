# coding=utf-8

from django.test import TestCase, Client
from django.test.client import RequestFactory

from hatter.models import Tecnico
from hatter.tests.test_models import create_provincia, create_estado, create_alerta, create_cliente, create_comunidad
from hatter.tests.test_models import create_prioridad, create_severidad, create_emplazamiento
from hatter.models import Actuacion

import json


def create_tecnico(nombre='Ana', apellidos='Belén Carro', dni='23278078P'):
    """
    tecnico test
    :param nombre:
    :param apellidos:
    :param dni:
    :return: tecnico
    """
    return Tecnico.objects.create(nombre=nombre, apellidos=apellidos, dni=dni)


def create_actuacion_direccion(nombre='Test1', direccion='Toledo, 97', codigo_postal=28005, tipo_via='Calle'):
    """
    actuacion test by address
    :param nombre:
    :param direccion:
    :param codigo_postal:
    :param tipo_via:
    :return: actuacion object
    """

    provincia = create_provincia()
    estado = create_estado()
    cliente = create_cliente()
    prioridad = create_prioridad()
    severidad = create_severidad()
    alerta = create_alerta()

    return Actuacion.objects.create(
        nombre=nombre,
        direccion=direccion,
        codigo_postal=codigo_postal,
        tipo_via=tipo_via,
        estado=estado,
        provincia=provincia,
        cliente=cliente,
        prioridad=prioridad,
        severidad=severidad,
        alerta=alerta
    )


def create_actuacion_emplazamiento(nombre='Test2'):
    """
    actuacion test by placement
    :param nombre:
    :return: actuacion object
    """

    estado = create_estado()
    cliente = create_cliente()
    prioridad = create_prioridad()
    severidad = create_severidad()
    alerta = create_alerta()
    emplazamiento = create_emplazamiento()

    return Actuacion.objects.create(
        nombre=nombre,
        emplazamiento=emplazamiento,
        estado=estado,
        cliente=cliente,
        prioridad=prioridad,
        severidad=severidad,
        alerta=alerta
    )


def create_actuacion_coordinates(nombre='Test3', longitud=34.12345, latitud=8.456123):
    """
    actuacion test by coordinates
    :param nombre:
    :param longitud:
    :param latitud:
    :return: actuacion object
    """

    estado = create_estado()
    cliente = create_cliente()
    prioridad = create_prioridad()
    severidad = create_severidad()
    alerta = create_alerta()

    return Actuacion.objects.create(
        nombre=nombre,
        longitud=longitud,
        latitud=latitud,
        cliente=cliente,
        estado=estado,
        prioridad=prioridad,
        severidad=severidad,
        alerta=alerta
    )


class AgendaTest(TestCase):
    """
    Agenda test case
    """
    def setUp(self):
        self.client = Client()

    def test_json_agenda(self):
        tecnico1 = create_tecnico()
        tecnico2 = create_tecnico()
        tecnico1.save()
        tecnico2.save()

        params = {
            'sDni': '65',
            'sName': 'Test'
        }

        data = {
            'jsonrpc': '2.0',
            'method': 'post',
            'params': {'sDni': '65', 'sName': 'Test'},
        }

        response = self.client.post('/getagendatecnico/', json.dumps(params), 'text/json', follow=True)

        self.assertEqual(response.status_code, 200)

    def test_json_turno(self):
        tecnico1 = create_tecnico()
        tecnico2 = create_tecnico()
        tecnico1.save()
        tecnico2.save()

        params = {

        }


class MapaTest(TestCase):
    """
    Mapa test case
    """
    def setUp(self):
        self.client = Client()

    def test_json_mapa(self):
        actuacion1 = create_actuacion_direccion()
        actuacion2 = create_actuacion_coordinates()
        actuacion3 = create_actuacion_emplazamiento()

        actuacion1.save()
        actuacion2.save()
        actuacion3.save()

        response = self.client.get('/getactuaciones/', follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.content), 164)
