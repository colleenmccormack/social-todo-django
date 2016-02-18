from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'up', views.say_whatsup, name='whatsup'),
    url(r'taskform', views.get_task, name='taskform'),
    url(r'nameform', views.get_name, name='nameform'),
    url(r'login/', auth_views.login, name='login'),
    url(r'logout/', auth_views.logout, name='logout'),
]

