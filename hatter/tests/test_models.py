from django.test import TestCase
from django.test import Client

from hatter.models import Actuacion


class ActuacionTestCase(TestCase):
    def setUp(self):
        Actuacion.objects.create(
            nombre='Test1',
            direccion='Moratines, 5',
            codigo_postal=28005,
            tipo_via='Calle',
            estado=1,
            provincia=31,
            prioridad=1,
            severidad=2,
            alerta=3,
            cliente=2
            )