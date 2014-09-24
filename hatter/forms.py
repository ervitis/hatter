# coding=utf-8

from django import forms

from hatter import models
from hatter.functions import validators

DEFAULT_ERROR_MESSAGES_REQUIRED = {
    'required': 'Este campo es obligatorio',
    'invalid':  'Compruebe este campo',
}

DEFAULT_ERROR_MESSAGES_NON_REQUIRED = {
    'invalid':  'Compruebe este campo'
}

INPUT_FORMAT_DATETIME = '%d/%m/%Y %H:%M:%S'
INPUT_FORMAT_DATE = '%d/%m/%Y'


class ActuacionForm(forms.ModelForm):
    """
    Clase formulario actuacion
    """

    VOID = ''
    CALLE = 'Calle'
    AVENIDA = 'Avda'
    PLAZA = 'Pza'
    TIPO_VIA_CHOICES = (
        (VOID, 'Escoja'),
        (CALLE, 'Calle'),
        (AVENIDA, 'Avenida'),
        (PLAZA, 'Plaza'),
    )

    nombre = forms.CharField(label='Nombre de la actuación', max_length=20, required=True, widget=forms.TextInput(attrs={
        'class':    'form-control',
        'required': 'true',
    }), error_messages=DEFAULT_ERROR_MESSAGES_REQUIRED)

    direccion = forms.CharField(label='Dirección', max_length=150, required=False, widget=forms.TextInput(attrs={
        'class':        'form-control',
        'placeholder':  'Introduzca la dirección',
    }), error_messages=DEFAULT_ERROR_MESSAGES_NON_REQUIRED)

    codigo_postal = forms.CharField(label='C.P', max_length=5, required=False, widget=forms.TextInput(attrs={
        'class': 'only-numbers form-control',
    }), validators=[validators.validate_codigo_postal], error_messages=DEFAULT_ERROR_MESSAGES_NON_REQUIRED)

    longitud = forms.FloatField(label='Longitud', max_value=180, min_value=-180, required=False, widget=forms.TextInput(attrs={
        'class': 'only-numbers form-control',
    }), error_messages=DEFAULT_ERROR_MESSAGES_NON_REQUIRED)

    latitud = forms.FloatField(label='Latitud', max_value=90, min_value=-90, required=False, widget=forms.TextInput(attrs={
        'class': 'only-numbers form-control',
    }), error_messages=DEFAULT_ERROR_MESSAGES_NON_REQUIRED)

    tipo_via = forms.ChoiceField(label='Tipo de vía', choices=TIPO_VIA_CHOICES, initial=VOID, required=False, widget=forms.Select(attrs={
        'class': 'form-control',
    }), error_messages=DEFAULT_ERROR_MESSAGES_NON_REQUIRED)

    estado = forms.ModelChoiceField(empty_label='Escoja un estado', required=True, label='Estado', queryset=models.Estado.objects.all(), widget=forms.Select(attrs={
        'class':    'form-control',
        'required': 'true',
    }), error_messages=DEFAULT_ERROR_MESSAGES_REQUIRED)

    cliente = forms.ModelChoiceField(empty_label='Escoja el tipo de cliente', required=True, label='Cliente', queryset=models.Cliente.objects.all(), widget=forms.Select(attrs={
        'class':    'form-control',
        'required': 'true',
    }), error_messages=DEFAULT_ERROR_MESSAGES_REQUIRED)

    provincia = forms.ModelChoiceField(empty_label='Escoja una provincia', label='Provincia', required=False, queryset=models.Provincia.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }), error_messages=DEFAULT_ERROR_MESSAGES_NON_REQUIRED)

    prioridad = forms.ModelChoiceField(empty_label='Escoja el nivel', required=True, label='Prioridad', queryset=models.Prioridad.objects.all(), widget=forms.Select(attrs={
        'class':    'form-control',
        'required': 'true',
    }), error_messages=DEFAULT_ERROR_MESSAGES_REQUIRED)

    severidad = forms.ModelChoiceField(empty_label='Escoja el nivel', required=True, label='Severidad', queryset=models.Severidad.objects.all(), widget=forms.Select(attrs={
        'class':    'form-control',
        'required': 'true',
    }), error_messages=DEFAULT_ERROR_MESSAGES_REQUIRED)

    alerta = forms.ModelChoiceField(empty_label='Escoja el nivel', required=True, label='Alerta', queryset=models.Alerta.objects.all(), widget=forms.Select(attrs={
        'class':    'form-control',
        'required': 'true',
    }), error_messages=DEFAULT_ERROR_MESSAGES_REQUIRED)

    emplazamiento = forms.ModelChoiceField(empty_label='Escoja el emplazamiento', label='Emplazamiento', required=False, queryset=models.Emplazamiento.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }), error_messages=DEFAULT_ERROR_MESSAGES_NON_REQUIRED)

    class Meta:
        model = models.Actuacion
        exclude = []


class TecnicoForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre', max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }), error_messages=DEFAULT_ERROR_MESSAGES_REQUIRED)

    apellidos = forms.CharField(label='Apellidos', max_length=150, required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }), error_messages=DEFAULT_ERROR_MESSAGES_NON_REQUIRED)

    dni = forms.CharField(label='DNI', max_length=9, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }), validators=[validators.validate_dni], error_messages=DEFAULT_ERROR_MESSAGES_REQUIRED)

    class Meta:
        model = models.Tecnico
        exclude = []


class DetalleActuacionForm(forms.ModelForm):
    fecha = forms.DateTimeField(input_formats=(INPUT_FORMAT_DATETIME,), label='Fecha', required=True, widget=forms.DateTimeInput(attrs={
        'class': 'form-control only-delete',
    }), error_messages=DEFAULT_ERROR_MESSAGES_REQUIRED)

    detalle = forms.CharField(label='Comentarios', required=False, max_length=1024, widget=forms.Textarea(attrs={
        'class':    'form-control',
        'rows':     '4',
        'cols':     '20',
        'style':    'resize:none;',
    }))

    class Meta:
        model = models.DetalleActuacion
        exclude = []


class TurnoForm(forms.ModelForm):
    fecha_inicio = forms.DateField(input_formats=INPUT_FORMAT_DATE, required=False, widget=forms.DateInput(attrs={
        'class': 'form-control only-delete mouse-pointer datetimepicker-input',
    }), error_messages=DEFAULT_ERROR_MESSAGES_REQUIRED)

    fecha_fin = forms.DateField(input_formats=INPUT_FORMAT_DATE, required=False, widget=forms.DateInput(attrs={
        'class': 'form-control only-delete mouse-pointer datetimepicker-input',
    }), error_messages=DEFAULT_ERROR_MESSAGES_REQUIRED)

    turnos = forms.ModelChoiceField(empty_label='Escoja turno', required=False, queryset=models.Turno.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
    }), error_messages=DEFAULT_ERROR_MESSAGES_REQUIRED)

    class Meta:
        model = models.Turno
        exclude = []
