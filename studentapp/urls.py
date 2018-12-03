from django.conf.urls import url

from studentapp import views

urlpatterns = [

    url(r'^student_123$', views.student_info),
]