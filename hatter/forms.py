# coding=utf-8

from django import forms

from hatter import models


class ActuacionForm(forms.Form):
    """
    Clase formulario actuacion
    """

    CALLE = 'C\\'
    AVENIDA = 'Avda'
    PLAZA = 'Pza'
    TIPO_VIA_CHOICES = (
        (CALLE, 'Calle'),
        (AVENIDA, 'Avenida'),
        (PLAZA, 'Plaza'),
    )

    nombre = forms.CharField(label='Nombre de la actuación', max_length=20, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    direccion = forms.CharField(label='Dirección', max_length=150, widget=forms.TextInput(attrs={
        'class':        'form-control',
        'placeholder':  'Introduzca la dirección',
    }))
    codigo_postal = forms.CharField(label='C.P', max_length=5, widget=forms.TextInput(attrs={
        'class': 'only-numbers form-control',
    }))
    longitud = forms.FloatField(label='Longitud', max_value=180, min_value=-180, widget=forms.TextInput(attrs={
        'class': 'only-numbers form-control',
    }))
    latitud = forms.FloatField(label='Latitud', max_value=90, min_value=-90, widget=forms.TextInput(attrs={
        'class': 'only-numbers form-control',
    }))
    tipo_via = forms.ChoiceField(label='Tipo de vía', choices=TIPO_VIA_CHOICES, initial=CALLE, widget=forms.Select(attrs={
        'class': 'form-control',
    }))
    estado = forms.ModelChoiceField(label='Estado', queryset=models.Estado.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }))
    cliente = forms.ModelChoiceField(label='Cliente', queryset=models.Cliente.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }))
    provincia = forms.ModelChoiceField(label='Provincia', queryset=models.Provincia.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }))
    prioridad = forms.ModelChoiceField(label='Prioridad', queryset=models.Prioridad.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }))
    severidad = forms.ModelChoiceField(label='Severidad', queryset=models.Severidad.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }))
    alerta = forms.ModelChoiceField(label='Alerta', queryset=models.Alerta.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }))
    emplazamiento = forms.ModelChoiceField(label='Emplazamiento', queryset=models.Emplazamiento.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }))
