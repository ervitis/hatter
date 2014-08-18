from django.db import models
from django.contrib.auth.models import User

import datetime


class Greeting(models.Model):
    author = models.ForeignKey(User, null=True, blank=True)
    content = models.CharField('Contenido')
    date = models.DateTimeField('Fecha publicada')
    utc = models.SlugField('utc')

    def __str__(self):
        return self.content

    def was_published_today(self):
        return self.date.date() == datetime.date.today()

    def get_datetime(self):
        return self.date.strftime("%d/%m/%Y %H:%M:%S")

    def get_utc(self):
        return self.utc

    def get_horas_minutos_utc(self):
        horas = int(self.utc[1:3])
        minutos = int(self.utc[3:])

        return {
            'horas':    horas,
            'minutos':  minutos,
        }

    def set_utc_from_dict(self, dict_h):
        if len(dict_h['horas']) == 1:
            dict_h['horas'] = '0' + dict_h['horas']

        if len(dict_h['minutos']) == 1:
            dict_h['minutos'] = '0' + dict_h['minutos']

        self.utc = dict_h['signo'] + dict_h['horas'] + ':' + dict_h['minutos']
