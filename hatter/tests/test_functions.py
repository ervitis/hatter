# coding=utf-8

from django.test import TestCase
from django.core.exceptions import ValidationError

from hatter.functions.validators import validate_codigo_postal, validate_dni
from hatter.functions import horario

import datetime

fmt_wo_utc = '%Y-%m-%d %H:%M:%S'


def create_utc_object(value):
    dict_utc = {
        'utc': value
    }

    return dict_utc


def create_time_object(value):
    dict_time = {
        'horas':    value[2:3],
        'minutos':  value[4:],
        'signo':    value[:1],
    }

    return dict_time


class ValidatorsTestCase(TestCase):
    """
    Validator test case
    """
    def test_codigo_postal(self):
        for i in range(1, 999):
            self.assertRaises(ValidationError, validate_codigo_postal, i)
        for i in range(53000, 99999):
            self.assertRaises(ValidationError, validate_codigo_postal, i)

    def test_dni(self):
        value1 = '012345678'
        value2 = '01234567'
        value3 = '0123456789'
        value4 = '03071978S'

        self.assertRaises(ValidationError, validate_dni, value1)
        self.assertRaises(ValidationError, validate_dni, value2)
        self.assertRaises(ValidationError, validate_dni, value3)
        self.assertRaises(ValidationError, validate_dni, value4)


class FunctionsTestCase(TestCase):
    """
    Functions test case
    """
    def test_get_horas(self):
        value_utc = create_utc_object('+0200')

        r = horario.get_horas_minutos_utc(value_utc)

        self.assertTrue(isinstance(r, dict))
        self.assertEqual(r['horas'], 2)
        self.assertEqual(r['minutos'], 0)

    def test_time(self):
        value_spain = horario.spain_timezone()
        self.assertTrue(isinstance(value_spain, datetime.datetime))

    def test_utc_from_dict(self):
        dict_time = create_time_object('+0200')

        r = horario.set_utc_from_dict(dict_time)
        self.assertTrue(isinstance(r, str))
        self.assertEqual(len(r), 6)
