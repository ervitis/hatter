# coding=utf-8

from django.core.exceptions import ValidationError

NOT_VALID_CP_MESSAGE = 'El código postal no es válido'


def validate_codigo_postal(value):

    v = int(value)

    if v < 1000 or v > 52999:
        raise ValidationError(NOT_VALID_CP_MESSAGE)
