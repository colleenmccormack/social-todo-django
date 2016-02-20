from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tasks, name='tasks'),
    url(r'^create', views.create, name='create'),
]

