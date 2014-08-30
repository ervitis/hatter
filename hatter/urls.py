from django.conf.urls import patterns, url
from functions.log import check_user

from hatter import views
from hatter.ws import map


urlpatterns = patterns('',
    url(r'^$', check_user(views.IndexView.as_view(template_name='index.html')), name='index'),
    url(r'^actuaciones/$', check_user(views.ActuacionesView.as_view(template_name='layout/actuaciones/listado.html')),
        name='listado_actuaciones'),
    url(r'^newactuacion/$', check_user(views.ActuacionesNewView.as_view()), name='new_actuacion'),
    url(r'^(?P<pk>\d+)/updateactuacion/$', check_user(views.ActuacionesUpdateView.as_view()), name='update_actuacion'),

    url(r'^mapa/$', check_user(views.MapaView.as_view()), name='mapa_view'),

    url(r'^tecnicos/$', check_user(views.TecnicosView.as_view()), name='listado_tecnicos'),
    url(r'^newtecnico/$', check_user(views.TecnicosNewView.as_view()), name='new_tecnico'),
    url(r'^(?P<pk>\d+)/updatetecnico/$', check_user(views.TecnicosUpdateView.as_view()), name='update_tecnico'),

    url(r'^getactuaciones/$', map.get_actuaciones, name='get_actuaciones_ws'),
)
