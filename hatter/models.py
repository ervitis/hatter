from django.db import models
from django.contrib.auth.models import User


class Estado(models.Model):
    """
    Clase estado
    """

    nombre = models.CharField('nombre', max_length=20)

    class Meta:
        db_table = 'estado'

    def __str__(self):
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


class Comunidad(models.Model):
    """
    Clase comunidad
    """

    nombre = models.CharField('nombre', max_length=150)

    class Meta:
        db_table = 'comunidad'

    def __str__(self):
        return self.nombre


class Provincia(models.Model):
    """
    Clase provincia
    """

    nombre = models.CharField('nombre', max_length=200)
    comunidad = models.ForeignKey(Comunidad, db_column='comunidad_id')

    class Meta:
        db_table = 'provincia'

    def __str__(self):
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


class Severidad(models.Model):
    """
    Clase severidad
    """

    nombre = models.CharField('nombre', max_length=50)

    class Meta:
        db_table = 'severidad'

    def __str__(self):
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


class Zona(models.Model):
    """
    Clase Zona
    """

    nombre = models.CharField('nombre', max_length=150)

    class Meta:
        db_table = 'zona'

    def __str__(self):
        return self.nombre


class Subzona(models.Model):
    """
    Clase subzona
    """

    nombre = models.CharField('nombre', max_length=150)
    zona = models.ForeignKey(Zona, db_column='zona_id')

    class Meta:
        db_table = 'subzona'

    def __str__(self):
        return self.nombre


class Actuacion(models.Model):
    """
    Clase actuacion
    """

    CALLE = 'C\\'
    AVENIDA = 'Avda'
    PLAZA = 'Pza'
    TIPO_VIA_CHOICES = (
        (CALLE, 'Calle'),
        (AVENIDA, 'Avenida'),
        (PLAZA, 'Plaza'),
    )

    nombre = models.CharField('nombre', max_length=20)
    direccion = models.CharField('direccion', max_length=150)
    codigo_postal = models.CharField('codigo postal', max_length=5)
    longitud = models.FloatField('longitud')
    latitud = models.FloatField('latitud')
    tipo_via = models.CharField('tipo de via', max_length=4, choices=TIPO_VIA_CHOICES, default=CALLE)
    estado = models.ForeignKey(Estado, db_column='estado_id')
    cliente = models.ForeignKey(Cliente, db_column='cliente_id')
    provincia = models.ForeignKey(Provincia, db_column='provincia_id')

    class Meta:
        db_table = 'actuacion'


class Instrumentacion(models.Model):
    """
    Clase instrumentacion
    """

    nombre = models.CharField('nombre', max_length=150)
    tecnologia = models.ForeignKey(Tecnologia, db_column='tecnologia_id')
    solucion = models.ManyToManyField(Actuacion, db_table='solucion')

    class Meta:
        db_table = 'instrumentacion'

    def __str__(self):
        return self.nombre



class Tecnico(models.Model):
    """
    Clase tecnico
    """

    nombre = models.CharField('nombre', max_length=50)
    apellidos = models.CharField('apellidos', max_length=150)
    dni = models.CharField('dni', max_length=10)
    username = models.ForeignKey(User)
    password = models.CharField('password', max_length=200)
    salt = models.CharField('salt', max_length=200)
    agenda = models.ManyToManyField(Turno, db_table='agenda')
    evento = models.ManyToManyField(Actuacion, db_table='evento')

    class Meta:
        db_table = 'tecnico'


class DetalleActuacion(models.Model):
    """
    Clase detalle actuacion
    """

    fecha_inicio = models.DateTimeField('fecha inicio')
    fecha_fin = models.DateTimeField('fecha fin')
    actuacion = models.OneToOneField(Actuacion, db_column='actuacion_id')
    utc = models.CharField('utc', max_length=75)
    detalle_actuacion = models.TextField('detalle', max_length=65536)

    class Meta:
        db_table = 'detalle_actuacion'


class Emplazamiento(models.Model):
    """
    Clase emplazamiento actuaciones
    """

    nombre = models.CharField('nombre', max_length=100)
    latitud = models.FloatField('latitud')
    longitud = models.FloatField('longitud')
    actuacion = models.ForeignKey(Actuacion, db_column='actuacion_id')

    class Meta:
        db_table = 'emplazamiento'
