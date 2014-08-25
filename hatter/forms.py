from django import forms


class ActuacionForm(forms.Form):
    """
    Clase formulario actuacion
    """

    nombre = forms.CharField(max_length=50)

