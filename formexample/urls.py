from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^forms$', views.form_example),
    url(r'^static_example$', views.staticExample)
]