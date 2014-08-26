from django.conf.urls import patterns, url

from hatter import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^actuaciones/$', views.ActuacionesView.as_view(), name='listado_actuaciones'),
    url(r'^newactuacion/$', views.new_actuacion, name='new_actuacion'),

)
