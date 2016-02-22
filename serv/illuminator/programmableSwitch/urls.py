from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^start/$', views.startServer, name='start'),
    url(r'^auth/$', views.auth, name='auth'),
    url(r'^log/$', views.displayLog, name='log'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^registerPoints/$', views.registerPoints, name='registerPoints'),
    url(r'^changeStates/$', views.changeStates, name='changeStates'),
]