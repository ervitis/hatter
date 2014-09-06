# coding=utf-8

from django.test import TestCase
from django.test import Client

from hatter import models


class ActuacionTestCase(TestCase):
    """
    Actuacion test case
    """

    def create_comunidad(self):
        return models.Comunidad.objects.create(nombre='Madrid')

    def create_estado(self):
        return models.Estado.objects.create(nombre='Abierto')

    def create_provincia(self):
        return models.Provincia.objects.create(comunidad=self.create_comunidad(), nombre='Madrid', codigo=28)

    def create_cliente(self):
        return models.Cliente.objects.create(nombre='ClientePrueba', prioridad=5)

    def create_severidad(self):
        return models.Severidad.objects.create(nombre='Normal')

    def create_alerta(self):
        return models.Alerta.objects.create(nombre='Normal', nivel_alerta=5)

    def create_prioridad(self):
        return models.Prioridad.objects.create(nombre='Normal', nivel_prioridad=5)

    def create_emplazamiento(self):
        return models.Emplazamiento.objects.create(nombre='EMP_Prueba', latitud=45.12, longitud=8.25,
                                                   provincia=self.create_provincia())

    def create_actuacion_direccion(self, nombre='Test1', direccion='Toledo, 97', codigo_postal=28005, tipo_via='Calle'):
        """
        actuacion test by address
        :param nombre:
        :param direccion:
        :param codigo_postal:
        :param tipo_via:
        :return: actuacion object
        """

        provincia = self.create_provincia()
        estado = self.create_estado()
        cliente = self.create_cliente()
        prioridad = self.create_prioridad()
        severidad = self.create_severidad()
        alerta = self.create_alerta()

        return models.Actuacion.objects.create(
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

    def create_actuacion_emplazamiento(self, nombre='Test2'):
        """
        actuacion test by placement
        :param nombre:
        :return: actuacion object
        """

        estado = self.create_estado()
        cliente = self.create_cliente()
        prioridad = self.create_prioridad()
        severidad = self.create_severidad()
        alerta = self.create_alerta()
        emplazamiento = self.create_emplazamiento()

        return models.Actuacion.objects.create(
            nombre=nombre,
            emplazamiento=emplazamiento,
            estado=estado,
            cliente=cliente,
            prioridad=prioridad,
            severidad=severidad,
            alerta=alerta
        )

    def create_actuacion_coordinates(self, nombre='Test3', longitud=34.12345, latitud=8.456123):
        """
        actuacion test by coordinates
        :param nombre:
        :param longitud:
        :param latitud:
        :return: actuacion object
        """

        estado = self.create_estado()
        cliente = self.create_cliente()
        prioridad = self.create_prioridad()
        severidad = self.create_severidad()
        alerta = self.create_alerta()

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

    def test_actuacion_creation_direccion(self):
        act1 = self.create_actuacion_direccion()
        self.assertTrue(isinstance(act1, models.Actuacion))
        self.assertEqual(act1.__unicode__(), act1.nombre)
        self.assertEqual(act1.__str__(), act1.nombre)

    def test_actuacion_creation_emplazamiento(self):
        act2 = self.create_actuacion_emplazamiento()
        self.assertTrue(isinstance(act2, models.Actuacion))
        self.assertTrue(act2.__unicode__(), act2.nombre)
        self.assertTrue(act2.__str__(), act2.nombre)

    def test_actuacion_creation_coordinates(self):
        act3 = self.create_actuacion_coordinates()
        self.assertTrue(isinstance(act3, models.Actuacion))
        self.assertTrue(act3.__unicode__(), act3.nombre)
        self.assertTrue(act3.__str__(), act3.nombre)


class TecnicoTestCase(TestCase):
    """
    Tecnico test case
    """

    def create_tecnico(self, nombre='Ana', apellidos='Belén Carro', dni='23278078P'):
        """
        tecnico test
        :param nombre:
        :param apellidos:
        :param dni:
        :return: tecnico
        """
        return models.Tecnico.objects.create(nombre=nombre, apellidos=apellidos, dni=dni)

    def test_tecnico_creation(self):
        tec = self.create_tecnico()
        self.assertTrue(isinstance(tec, models.Tecnico))
        self.assertEqual(tec.__unicode__(), tec.nombre)
        self.assertEqual(tec.__str__(), tec.nombre)
