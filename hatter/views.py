from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from datetime import datetime

from models import Actuacion

from pytz import timezone
import logging

fmt = '%Y-%m-%d %H:%M:%S %Z%z'
fmt_wo_utc = '%Y-%m-%d %H:%M:%S'


class IndexView(generic.ListView):
    model = Actuacion
    template_name = 'index.html'


class DetailView(generic.DetailView):
    template_name = 'detail.html'


class ResultsView(generic.DetailView):
    template_name = 'results.html'


def newview(request):
    users = User.objects.order_by('username')

    return render_to_response('new.html', {
        'users': users,
    }, RequestContext(request))
