from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from datetime import datetime

from hatter.models import Greeting
from pytz import timezone
import logging

fmt = '%Y-%m-%d %H:%M:%S %Z%z'
fmt_wo_utc = '%Y-%m-%d %H:%M:%S'


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_greeting_list'
    paginate_by = 15
    queryset = Greeting.objects.order_by('date')


class DetailView(generic.DetailView):
    model = Greeting
    template_name = 'detail.html'


class ResultsView(generic.DetailView):
    model = Greeting
    template_name = 'results.html'


def newview(request):
    users = User.objects.order_by('username')

    return render_to_response('new.html', {
        'users': users,
    }, RequestContext(request))


def savenew(request):
    if request.POST['content']:
        greeting = Greeting()
        greeting.author = search_user(request.POST['users'])
        greeting.content = request.POST['content']

        date_with_utc = spain_timezone()
        dic_date = get_datetime_utc(date_with_utc.strftime(fmt))
        greeting.date = dic_date['v_horamin']
        Greeting.set_utc_from_dict(greeting, dic_date['v_utc'])

        greeting.save()

        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('index'))


def vote(request, greeting_id):
    g = get_object_or_404(Greeting, pk=greeting_id)

    try:
        content = request.POST['content']
        g.content = content
    except (KeyError, Greeting.DoesNotExist):
        return render(request, 'detail.html', {
            'greeting':         g,
            'error_message':    'No se ha seleccionado nada',
        })
    else:
        g.save()

    return HttpResponseRedirect(reverse('results', args=(g.id,)))


def search_user(name):
    return User.objects.get(username=name)


def spain_timezone():
    fecha_actual_utc = datetime.now(timezone('UTC'))

    # Convert to Spain local time
    now_spain = fecha_actual_utc.astimezone(timezone('Europe/Madrid'))

    return now_spain


def get_datetime_utc(time):
    # Separate time and utc
    utc = time[-5:]

    utc = {
        'signo':    utc[:1],
        'horas':    utc[2:3],
        'minutos':  utc[4:],
    }

    date_time = time[:-10]

    return {
        'v_utc':        utc,
        'v_horamin':    datetime.strptime(date_time, fmt_wo_utc),
    }
