from django.conf.urls import url

from . import views

app_name = 'home'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.home, name='home'),
]
