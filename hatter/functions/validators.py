# coding=utf-8

from django.core.exceptions import ValidationError

NOT_VALID_CP_MESSAGE = 'El código postal no es válido'
NOT_VALID_DNI_MESSAGE = 'La letra del DNI no coincide con la serie numérica'
DNI_TOO_SHORT = 'El DNI debe tener una longitud de 8 números y una letra'


def validate_codigo_postal(value):

    v = int(value)

    if v < 1000 or v > 52999:
        raise ValidationError(NOT_VALID_CP_MESSAGE)


def validate_dni(value):
    if len(value) != 9:
        raise ValidationError(DNI_TOO_SHORT)

    nif = 'TRWAGMYFPDXBNJZSQVHLCKE'

    l = value[8:]
    n = int(value[:8])

    ln = nif[n % 23]

    if ln != l:
        raise ValidationError(NOT_VALID_DNI_MESSAGE)
