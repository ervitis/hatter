from django.db import models
from django.contrib.auth.models import User

import datetime


class Greeting(models.Model):
    author = models.ForeignKey(User, null=True, blank=True)
    content = models.SlugField('Contenido')
    date = models.DateTimeField('Fecha publicada')

    def __str__(self):
        return self.content

    def was_published_today(self):
        return self.date.date() == datetime.date.today()

    def get_datetime(self):
        return self.date.strftime("%d/%m/%Y %H:%M:%S")
