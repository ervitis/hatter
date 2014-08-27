from django.conf.urls import patterns, url

from hatter import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^actuaciones/$', views.ActuacionesView.as_view(), name='listado_actuaciones'),
    url(r'^formactuacion/$', views.ActuacionesFormView.as_view(), name='formulario_actuaciones'),
)
