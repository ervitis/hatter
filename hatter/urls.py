from django.conf.urls import patterns, url
from functions.log import check_user
from django.views.decorators.csrf import ensure_csrf_cookie

from hatter import views
from hatter.ws import map, agenda


urlpatterns = patterns('',
    url(r'^$', check_user(views.IndexView.as_view(template_name='index.html')), name='index'),
    url(r'^actuaciones/$', check_user(views.ActuacionesView.as_view(template_name='layout/actuaciones/actuaciones.html')),
        name='listado_actuaciones'),
    url(r'^newactuacion/$', views.actuaciones_new_view, name='new_actuacion'),
    url(r'^(?P<actuacion_id>\d+)/updateactuacion/$', views.actuaciones_update_view, name='update_actuacion'),

    url(r'^mapa/$', check_user(views.MapaView.as_view()), name='mapa_view'),

    url(r'^tecnicos/$', check_user(views.TecnicosView.as_view()), name='listado_tecnicos'),
    url(r'^newtecnico/$', check_user(views.TecnicosNewView.as_view()), name='new_tecnico'),
    url(r'^(?P<pk>\d+)/updatetecnico/$', check_user(views.TecnicosUpdateView.as_view()), name='update_tecnico'),

    url(r'^tools/$', check_user(views.ToolsView.as_view()), name='tools_view'),
    url(r'^tools/searchtecnico', views.listado_tecnicos, name='tools_listado_tecnicos'),
    url(r'^tools/saveturnos', views.save_turnos, name='tools_save_turnos'),

    url(r'^getagendatecnico/$', ensure_csrf_cookie(agenda.search_agenda_tecnico), name='listado_agenda'),
    url(r'^getactuaciones/$', map.get_actuaciones, name='get_actuaciones_ws'),
    url(r'^getturnotecnico/$', ensure_csrf_cookie(agenda.search_turnos_tecnico), name='listado_turno'),
    url(r'^asignaactuacion/$', ensure_csrf_cookie(agenda.asigna_actuacion_tecnico), name='asigna_actuacion'),
)
