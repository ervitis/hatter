# coding=utf-8

from django.test import TestCase

from hatter import models
from hatter.functions.horario import spain_timezone
import datetime


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


def create_emplazamiento():
    return models.Emplazamiento.objects.create(nombre='EMP_Prueba', latitud=45.12, longitud=8.25,
                                               provincia=create_provincia())


def create_turno():
    return models.Turno.objects.create(nombre='tn1', hora_inicio='12:00:00', hora_fin='20:30:00')


def create_tecnologia():
    return models.Tecnologia.objects.create(nombre='tecnología1')


def create_instrumentacion():
    return models.Instrumentacion.objects.create(nombre='instrumentación1', tecnologia=create_tecnologia())


def create_detalle_actuacion(actuacion):
    return models.DetalleActuacion.objects.create(
        actuacion=actuacion,
        fecha=spain_timezone(),
        utc='+0200',
        detalle='Un test')


def create_agenda(tecnico):
    return models.Agenda.objects.create(tecnico=tecnico, turno=create_turno(), fecha=datetime.date.today())


def create_tecnico(nombre='Ana', apellidos='Belén Carro', dni='23278078P'):
    return models.Tecnico.objects.create(nombre=nombre, apellidos=apellidos, dni=dni)


def create_actuacion_emplazamiento(nombre='Test2'):
        estado = create_estado()
        cliente = create_cliente()
        prioridad = create_prioridad()
        severidad = create_severidad()
        alerta = create_alerta()
        emplazamiento = create_emplazamiento()

        return models.Actuacion.objects.create(
            nombre=nombre,
            emplazamiento=emplazamiento,
            estado=estado,
            cliente=cliente,
            prioridad=prioridad,
            severidad=severidad,
            alerta=alerta
        )


class EstadoTestCase(TestCase):
    """
    Estado test case
    """
    def test_estado(self):
        estado = create_estado()
        self.assertTrue(isinstance(estado, models.Estado))
        self.assertEqual(estado.__unicode__(), estado.nombre)
        self.assertEqual(estado.__str__(), estado.nombre)


class ClienteTestCase(TestCase):
    """
    Cliente test case
    """
    def test_cliente(self):
        cliente = create_cliente()
        self.assertTrue(isinstance(cliente, models.Cliente))
        self.assertEqual(cliente.__unicode__(), cliente.nombre)
        self.assertEqual(cliente.__str__(), cliente.nombre)


class TurnoTestCase(TestCase):
    """
    Turno test case
    """
    def test_turno(self):
        turno = create_turno()
        self.assertTrue(isinstance(turno, models.Turno))
        self.assertEqual(turno.__str__(), turno.nombre)
        self.assertEqual(turno.__unicode__(), turno.nombre)


class ComunidadTestCase(TestCase):
    """
    Comunidad test case
    """
    def test_comunidad(self):
        comunidad = create_comunidad()
        self.assertTrue(isinstance(comunidad, models.Comunidad))
        self.assertEqual(comunidad.__str__(), comunidad.nombre)
        self.assertEqual(comunidad.__unicode__(), comunidad.nombre)


class ProvinciaTestCase(TestCase):
    """
    Provincia test case
    """
    def test_provincia(self):
        provincia = create_provincia()
        self.assertTrue(isinstance(provincia, models.Provincia))
        self.assertEqual(provincia.__unicode__(), provincia.nombre)
        self.assertEqual(provincia.__str__(), provincia.nombre)


class TecnologiaTestCase(TestCase):
    """
    Tecnologia test case
    """
    def test_tecnologia(self):
        tecnologia = create_tecnologia()
        self.assertTrue(isinstance(tecnologia, models.Tecnologia))
        self.assertEqual(tecnologia.__unicode__(), tecnologia.nombre)
        self.assertEqual(tecnologia.__str__(), tecnologia.nombre)


class SeveridadTestCase(TestCase):
    """
    Severidad test case
    """
    def test_severidad(self):
        severidad = create_severidad()
        self.assertTrue(isinstance(severidad, models.Severidad))
        self.assertEqual(severidad.__unicode__(), severidad.nombre)
        self.assertEqual(severidad.__str__(), severidad.nombre)


class PrioridadTestCase(TestCase):
    """
    Prioridad test case
    """
    def test_prioridad(self):
        prioridad = create_prioridad()
        self.assertTrue(isinstance(prioridad, models.Prioridad))
        self.assertEqual(prioridad.__unicode__(), prioridad.nombre)
        self.assertEqual(prioridad.__str__(), prioridad.nombre)


class AlertaTestCase(TestCase):
    """
    Alerta test case
    """
    def test_alerta(self):
        alerta = create_alerta()
        self.assertTrue(isinstance(alerta, models.Alerta))
        self.assertEqual(alerta.__str__(), alerta.nombre)
        self.assertEqual(alerta.__unicode__(), alerta.nombre)


class EmplazamientoTestCase(TestCase):
    """
    Emplazamiento test case
    """
    def test_emplazamiento(self):
        emplazamiento = create_emplazamiento()
        self.assertTrue(isinstance(emplazamiento, models.Emplazamiento))
        self.assertEqual(emplazamiento.__unicode__(), emplazamiento.nombre)


class InstrumentacionTestCase(TestCase):
    """
    Instrumentacion test case
    """
    def test_instrumentacion(self):
        instrumentacion = create_instrumentacion()
        self.assertTrue(isinstance(instrumentacion, models.Instrumentacion))
        self.assertEqual(instrumentacion.__unicode__(), instrumentacion.nombre)
        self.assertEqual(instrumentacion.__str__(), instrumentacion.nombre)


class ActuacionTestCase(TestCase):
    """
    Actuacion test case
    """

    def create_actuacion_direccion(self, nombre='Test1', direccion='Toledo, 97', codigo_postal=28005, tipo_via='Calle'):
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

    def create_actuacion_coordinates(self, nombre='Test3', longitud=34.12345, latitud=8.456123):
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

    def test_actuacion_creation_direccion(self):
        act1 = self.create_actuacion_direccion()
        self.assertTrue(isinstance(act1, models.Actuacion))
        self.assertEqual(act1.__unicode__(), act1.nombre)
        self.assertEqual(act1.__str__(), act1.nombre)

    def test_actuacion_creation_emplazamiento(self):
        act2 = create_actuacion_emplazamiento()
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

    def test_tecnico_creation(self):
        tec = create_tecnico()
        tec.save()
        self.assertTrue(isinstance(tec, models.Tecnico))
        self.assertEqual(tec.__unicode__(), tec.nombre)
        self.assertEqual(tec.__str__(), tec.nombre)


class DetalleActuacionTestCase(TestCase):
    """
    Detalle actuación test case
    """

    def test_detalle_actuacion(self):
        actuacion = create_actuacion_emplazamiento()
        detalle_actuacion = create_detalle_actuacion(actuacion=actuacion)

        self.assertTrue(isinstance(detalle_actuacion, models.DetalleActuacion))
        self.assertTrue(isinstance(actuacion, models.Actuacion))
        self.assertTrue(isinstance(detalle_actuacion.fecha, datetime.datetime))


class AgendaTestCase(TestCase):
    """
    Agenda test case
    """

    def test_agenda(self):
        tecnico = create_tecnico()
        agenda = create_agenda(tecnico=tecnico)

        self.assertTrue(isinstance(agenda, models.Agenda))
        self.assertTrue(isinstance(agenda.fecha, datetime.date))
