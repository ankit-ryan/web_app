from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create$', views.create),
    url(r'^index$',views.index),
    url(r'^update$',views.update),
    url(r'^delete$',views.delete),
    url(r'^view$',views.view)
]