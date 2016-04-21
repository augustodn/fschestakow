from django.conf.urls import url

from . import views

app_name = 'farmacias'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pharmacy_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^turnos/$', views.shift, name='shift'),
]
