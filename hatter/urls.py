from django.conf.urls import patterns, url

from hatter import views
from hatter.ws import map


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^actuaciones/$', views.ActuacionesView.as_view(), name='listado_actuaciones'),
    url(r'^newactuacion/$', views.ActuacionesNewView.as_view(), name='new_actuacion'),
    url(r'^(?P<pk>\d+)/updateactuacion/$', views.ActuacionesUpdateView.as_view(), name='update_actuacion'),

    url(r'^mapa/$', views.MapaView.as_view(), name='mapa_view'),

    url(r'^getactuaciones/$', map.get_actuaciones, name='get_actuaciones_ws'),
)
