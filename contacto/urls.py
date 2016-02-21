from django.conf.urls import url

from . import views

app_name = 'contacto'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.contact_form, name='contact_form'),
]
