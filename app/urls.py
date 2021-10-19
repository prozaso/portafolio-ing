from django.urls import path
from .views import views, servicios, usuarios, capacitaciones, rubros, contratos


urlpatterns = [
    path('', views.home, name="home"),
    path('servicios', servicios.servicios, name="servicios"),
    path('registro_usuarios', usuarios.registro_usuarios, name='registro_usuarios'),
    path('capacitaciones', capacitaciones.capacitaciones, name='capacitaciones'),
    path('rubros', rubros.rubros, name='rubros'),
    path('contratos', contratos.contratos, name='contratos')

]