from django.urls import path

from app.views.accidentes import accidentes
from .views import views, servicios, usuarios, capacitaciones, rubros, contratos, accidentes


urlpatterns = [
    path('', views.home, name="home"),
    path('servicios', servicios.servicios, name="servicios"),
    path('registro_usuarios', usuarios.registro_usuarios, name='registro_usuarios'),
    path('capacitaciones', capacitaciones.capacitaciones, name='capacitaciones'),
    path('rubros', rubros.rubros, name='rubros'),
    path('contratos', contratos.contratos, name='contratos'),
    path('comunas/', contratos.select_comuna_por_region, name='select_comuna_por_region'),
    path('accidentes', accidentes.accidentes, name='accidentes'),

]