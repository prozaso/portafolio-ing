from django.conf.urls import url
from django.urls import path
from app import views
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('servicios', servicios, name="servicios"),


]