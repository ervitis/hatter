# coding=utf-8

from django.db import models
from django.db.models import Q, Count
from django.db import DEFAULT_DB_ALIAS

import logging


class Estado(models.Model):
    """
    Clase estado
    """

    nombre = models.CharField('nombre', max_length=20)

    class Meta:
        db_table = 'estado'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


class Cliente(models.Model):
    """
    Clase cliente
    """

    nombre = models.CharField('nombre', max_length=50)
    prioridad = models.IntegerField('prioridad', max_length=10)

    class Meta:
        db_table = 'cliente'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


class Turno(models.Model):
    """
    Clase turno
    """

    nombre = models.CharField('nombre', max_length=50)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        db_table = 'turno'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


class Comunidad(models.Model):
    """
    Clase comunidad
    """

    nombre = models.CharField('nombre', max_length=150)

    class Meta:
        db_table = 'comunidad'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


class Provincia(models.Model):
    """
    Clase provincia
    """

    nombre = models.CharField('nombre', max_length=200)
    comunidad = models.ForeignKey(Comunidad, db_column='comunidad_id')
    codigo = models.IntegerField('codigo', max_length=10)

    class Meta:
        db_table = 'provincia'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


class Tecnologia(models.Model):
    """
    Clase tecnologia
    """

    nombre = models.CharField('nombre', max_length=200)

    class Meta:
        db_table = 'tecnologia'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


class Severidad(models.Model):
    """
    Clase severidad
    """

    nombre = models.CharField('nombre', max_length=50)

    class Meta:
        db_table = 'severidad'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


class Prioridad(models.Model):
    """
    Clase prioridad
    """

    nombre = models.CharField('nombre', max_length=50)
    nivel_prioridad = models.PositiveIntegerField('nivel_prioridad', max_length=10)

    class Meta:
        db_table = 'prioridad'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


class Alerta(models.Model):
    """
    Clase alerta
    """

    nombre = models.CharField('nombre', max_length=50)
    nivel_alerta = models.PositiveIntegerField('nivel_alerta', max_length=10)

    class Meta:
        db_table = 'alerta'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


class Emplazamiento(models.Model):
    """
    Clase emplazamiento actuaciones
    """

    nombre = models.CharField('nombre', max_length=100)
    latitud = models.FloatField('latitud')
    longitud = models.FloatField('longitud')
    provincia = models.ForeignKey(Provincia, db_column='provincia_id')

    class Meta:
        db_table = 'emplazamiento'

    def __unicode__(self):
        return self.nombre


class Actuacion(models.Model):
    """
    Clase actuacion
    """

    from hatter.functions import validators

    VOID = ''
    CALLE = 'Calle'
    AVENIDA = 'Avda'
    PLAZA = 'Pza'
    TIPO_VIA_CHOICES = (
        (VOID, ''),
        (CALLE, 'Calle'),
        (AVENIDA, 'Avenida'),
        (PLAZA, 'Plaza'),
    )

    nombre = models.CharField('nombre', max_length=20)
    direccion = models.CharField('direccion', max_length=150, default=None, null=True)
    codigo_postal = models.CharField('codigo postal', max_length=5, default=None, null=True, validators=[validators.validate_codigo_postal])
    longitud = models.FloatField('longitud', default=None, null=True)
    latitud = models.FloatField('latitud', default=None, null=True)
    tipo_via = models.CharField('tipo de via', max_length=5, choices=TIPO_VIA_CHOICES, default=VOID)
    estado = models.ForeignKey(Estado, db_column='estado_id')
    cliente = models.ForeignKey(Cliente, db_column='cliente_id')
    provincia = models.ForeignKey(Provincia, db_column='provincia_id', null=True)
    emplazamiento = models.ForeignKey(Emplazamiento, db_column='emplazamiento_id', null=True)
    prioridad = models.ForeignKey(Prioridad, db_column='prioridad_id')
    severidad = models.ForeignKey(Severidad, db_column='severidad_id')
    alerta = models.ForeignKey(Alerta, db_column='alerta_id')

    class Meta:
        db_table = 'actuacion'

    def __unicode__(self):
        return self.nombre


class Instrumentacion(models.Model):
    """
    Clase instrumentacion
    """

    nombre = models.CharField('nombre', max_length=150)
    tecnologia = models.ForeignKey(Tecnologia, db_column='tecnologia_id')
    solucion = models.ManyToManyField(Actuacion, db_table='solucion', null=True, blank=True)

    class Meta:
        db_table = 'instrumentacion'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


class Tecnico(models.Model):
    """
    Clase tecnico
    """

    nombre = models.CharField('nombre', max_length=50)
    apellidos = models.CharField('apellidos', max_length=150, null=True)
    dni = models.CharField('dni', max_length=9)
    evento = models.ManyToManyField(Actuacion, db_table='evento', blank=True)

    class Meta:
        db_table = 'tecnico'

    def __unicode__(self):
        return self.nombre

    def get_eventos_by_tecnico_data(self, nombre, fecha):
        """
        :param nombre del técnico
        :param dni del técnico
        :return array evento__actuacion
        """

        query = self.__class__.objects.select_related('evento__actuacion').filter(
            Q(evento__tecnico__nombre__contains=nombre) |
            Q(evento__tecnico__apellidos__contains=nombre) &
            Q(evento__detalleactuacion__fecha_inicio__lte=fecha) &
            Q(evento__detalleactuacion__fecha_fin__gte=fecha) &
            Q(evento__isnull=False)
        ).values(
            'id', 'nombre', 'apellidos',
            'evento__detalleactuacion__fecha_inicio', 'evento__detalleactuacion__fecha_fin', 'evento__id',
            'evento__estado__id'
        )[:5]

        return query


class DetalleActuacion(models.Model):
    """
    Clase detalle actuacion
    """

    fecha_inicio = models.DateTimeField('fecha_inicio')
    fecha_fin = models.DateTimeField('fecha_fin', blank=True, null=True)
    actuacion = models.OneToOneField(Actuacion, blank=True, null=True)
    utc = models.CharField('utc', max_length=75, blank=True, null=True)
    detalle = models.CharField('detalle', max_length=1023, blank=True, null=True)

    class Meta:
        db_table = 'detalle_actuacion'


class Agenda(models.Model):
    """
    Clase agenda
    """

    tecnico = models.ForeignKey(Tecnico, blank=True, null=True)
    turno = models.ForeignKey(Turno, blank=True, null=True)
    fecha = models.DateField('fecha')

    class Meta:
        db_table = 'agenda'

    def get_tecnico_in_agenda(self, nombre, fecha):
        """
        :param nombre del técnico
        :param dni del técnico
        :return array agenda__tecnico
        """

        nombre = '%' + nombre + '%'

        query = self.__class__.objects.raw('''
            select ag.id, tec.id as tecnico__id
            from tecnico tec
            inner join agenda ag on ag.tecnico_id = tec.id
            where tec.nombre like %s or tec.apellidos like %s and ag.fecha = %s
            group by tec.id
        ''', [nombre, nombre, fecha])

        return query

    def get_turnos_by_tecnico(self, tecnico_id, fecha):
        """
        :param tecnico_id:
        :param fecha:
        :return:
        """
        query = self.__class__.objects.raw('''
            select tu.id, tu.hora_inicio as turno__hora_inicio, tu.hora_fin as turno__hora_fin
            from turno tu
            inner join agenda ag on ag.turno_id = tu.id
            inner join tecnico tec on tec.id = ag.tecnico_id
            where ag.fecha = %s and tec.id = %s
        ''', [fecha, tecnico_id])

        return query
