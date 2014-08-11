from django.shortcuts import render
from django.core.cache import cache
from django.views import generic
from hatter.models import Greeting
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

from hatter.models import Greeting


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_greeting_list'
    paginate_by = 5
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
        greeting.date = timezone.make_aware(datetime.now(), timezone.get_current_timezone())

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
