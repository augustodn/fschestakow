from django.conf.urls import url

from . import views

app_name = 'about us'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.about_us, name='about_us'),
]
