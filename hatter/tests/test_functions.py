# coding=utf-8

from django.test import TestCase
from django.core.exceptions import ValidationError

from hatter.functions.validators import validate_codigo_postal, validate_dni


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
