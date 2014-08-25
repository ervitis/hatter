from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from models import Actuacion


import logging


class IndexView(generic.TemplateView):
    """
    Index
    """

    template_name = 'index.html'


class ActuacionesView(generic.ListView):
    """
    Get the list of tasks
    """

    template_name = 'layout/actuaciones/listado.html'
    context_object_name = 'listado_actuaciones'
    paginate_by = 10
    queryset = Actuacion.objects.order_by('id')


def new_actuacion(request):
    if request.method == 'POST':

