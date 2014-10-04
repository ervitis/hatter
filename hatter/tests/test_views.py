# coding=utf-8

from django.test import TestCase
from django.test.client import RequestFactory

from hatter import models, forms, views

from google.appengine.api import users
from datetime import datetime

import os


def set_current_user_testing(email='test@gmail.com', user_id='1', is_admin=False):
    os.environ['USER_EMAIL'] = email
    os.environ['USER_ID'] = user_id
    os.environ['USER_IS_ADMIN'] = '1' if is_admin else '0'
    os.environ['AUTH_DOMAIN'] = 'testing'


def create_comunidad():
    return models.Comunidad.objects.create(nombre='Madrid')


def create_estado():
    return models.Estado.objects.create(nombre='Abierto')


def create_provincia():
    return models.Provincia.objects.create(comunidad=create_comunidad(), nombre='Madrid', codigo=28)


def create_cliente():
    return models.Cliente.objects.create(nombre='ClientePrueba', prioridad=5)


def create_severidad():
    return models.Severidad.objects.create(nombre='Normal')


def create_alerta():
    return models.Alerta.objects.create(nombre='Normal', nivel_alerta=5)


def create_prioridad():
    return models.Prioridad.objects.create(nombre='Normal', nivel_prioridad=5)


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

        return models.Actuacion.objects.create(
            nombre=nombre,
            longitud=longitud,
            latitud=latitud,
            cliente=cliente,
            estado=estado,
            prioridad=prioridad,
            severidad=severidad,
            alerta=alerta
        )


class ViewsTestCase(TestCase):
    """
    Views test case
    """
    def setUp(self):
        set_current_user_testing(email='test@gmail.com', user_id='1')
        self.factory= RequestFactory()
        self.user = users.get_current_user()

    def test_index(self):
        request = self.factory.get('/')
        request.user = self.user

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_list_actuaciones(self):
        actuacion = create_actuacion_coordinates()
        actuacion.save()

        response = self.client.get('/actuaciones/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('listado_actuaciones' in response.context)
        self.assertEqual([actuacion.pk for actuacion in response.context['listado_actuaciones']], [5L])

    def test_list_tecnicos(self):
        response = self.client.get('/tecnicos/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('listado_tecnicos' in response.context)

    def test_new_tecnico_valid(self):
        tecnico1 = models.Tecnico(nombre='Pepe', apellidos='Garcia Fili', dni='33186203D')

        data = {
            'nombre':    tecnico1.nombre,
            'apellidos': tecnico1.apellidos,
            'dni':       tecnico1.dni,
        }

        form = forms.TecnicoForm(data=data, instance=tecnico1)

        self.assertTrue(form.is_valid())

    def test_new_tecnico_invalid(self):
        tecnico2 = models.Tecnico(nombre='Pepa', apellidos='Garcias Feliz', dni='31234584F')
        tecnico3 = models.Tecnico(nombre='Pepas', apellidos='Garcias Felice', dni='3123458F')

        data = {
            'nombre':    tecnico2.nombre,
            'apellidos': tecnico2.apellidos,
            'dni':       tecnico2.dni,
        }

        form = forms.TecnicoForm(data=data)
        self.assertFalse(form.is_valid())

        data = {
            'nombre':    tecnico3.nombre,
            'apellidos': tecnico3.apellidos,
            'dni':       tecnico3.dni,
        }

        form = forms.TecnicoForm(data=data)
        self.assertFalse(form.is_valid())

    def test_listado_turnos(self):
        tecnico = models.Tecnico(nombre='Pepa', apellidos='Garcias Feliz', dni='31234584F')
        tecnico.save()

        turno = models.Turno(nombre='P2', hora_inicio='12:00', hora_fin='20:00')
        turno.save()

        agenda = models.Agenda.objects.create(tecnico=tecnico, turno=turno, fecha=datetime.now().date())
        agenda.save()

        data = {
            'turnoNombre': tecnico.nombre,
            'turnoDni': tecnico.dni
        }

        request_factory = RequestFactory()
        request = request_factory.post(path='/getturnotecnico', data=data)

        response = views.listado_tecnicos(request)

        self.assertEqual(response.status_code, 200)

