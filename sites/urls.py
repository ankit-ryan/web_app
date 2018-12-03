from django.conf.urls import url
from sites import views

urlpatterns = [

    url(r'^registration$',views.userRegistration),
    url(r'^login$',views.userLogin),
    url(r'^dashboard$',views.dashBoard),
    url(r'^logout$',views.userLogout),

]