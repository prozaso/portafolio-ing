from django.conf.urls import url
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('servicios', servicios, name="servicios"),
    path('registro_usuarios', registro_usuarios, name='registro_usuarios'),

]