from django.urls import path

from app.views.accidentes import accidentes
from app.views.registro_capacitaciones import registro_capacitaciones
from .views import views, servicios, usuarios, capacitaciones, rubros, contratos, accidentes, perfil_cliente, registro_capacitaciones, perfil_profesional, visita_revision


urlpatterns = [
    path('', views.home, name="home"),
    path('servicios', servicios.servicios, name="servicios"),
    path('registro_usuarios', usuarios.registro_usuarios, name='registro_usuarios'),
    path('capacitaciones', capacitaciones.capacitaciones, name='capacitaciones'),
    path('rubros', rubros.rubros, name='rubros'),
    path('contratos', contratos.contratos, name='contratos'),
    path('comunas/', contratos.select_comuna_por_region, name='select_comuna_por_region'),
    path('accidentes', accidentes.accidentes, name='accidentes'),
    path('perfil_cliente', perfil_cliente.perfil_cliente, name='perfil_cliente'),
    path('registro_capacitaciones', registro_capacitaciones.registro_capacitaciones, name='registro_capacitaciones'),
    path('perfil_profesional', perfil_profesional.perfil_profesional, name='perfil_profesional'),
    path('visita_revision', visita_revision.visita_revision, name='visita_revision'),

]