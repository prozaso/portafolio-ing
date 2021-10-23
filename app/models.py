from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.


class User(AbstractUser):
    es_administrador    = models.BooleanField('Es administrador', default=False)
    es_profesional      = models.BooleanField('Es profesional', default=False)
    es_cliente          = models.BooleanField('Es cliente', default=False)
    rut                 = models.CharField(max_length=10, null=False)
    email               = models.EmailField(max_length=100, unique=True, null=False)
    razon_social        = models.CharField(max_length=300, null=True, blank=True)

    phoneNumberRegex    = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    telefono            = models.CharField(validators = [phoneNumberRegex], max_length = 12, null=True)
    direccion           = models.CharField(max_length=300, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Accidente(models.Model):
    id_accidente = models.BigIntegerField(primary_key=True)
    fecha_acc = models.CharField(max_length=10)
    alerta = models.FloatField()
    tipo_accidente_id_tipo_acc = models.ForeignKey('TipoAccidente', models.DO_NOTHING, db_column='tipo_accidente_id_tipo_acc', blank=True, null=True)
    contrato_cliente_id_contrato = models.ForeignKey('ContratoCliente', models.DO_NOTHING, db_column='contrato_cliente_id_contrato', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accidente'


class AlertaCumplimiento(models.Model):
    id_alerta_cum = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'alerta_cumplimiento'


class Capacitacion(models.Model):
    id_capacitacion = models.FloatField(primary_key=True)
    nombre_cap = models.CharField(max_length=100)
    fecha_cap = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'capacitacion'


class Comuna(models.Model):
    id_comuna = models.FloatField(primary_key=True)
    region_id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region_id_region')
    nombre_comuna = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'comuna'


class Condicion(models.Model):
    id_condicion = models.FloatField(primary_key=True)
    servicio_id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='servicio_id_servicio', blank=True, null=True)
    nombre_condicion = models.CharField(max_length=200, blank=True, null=True)
    detalle_condicion = models.CharField(max_length=1000)
    valor_condicion = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'condicion'


class ContratoCliente(models.Model):
    id_contrato = models.FloatField(primary_key=True)
    rubro_id_rubro = models.ForeignKey('Rubro', models.DO_NOTHING, db_column='rubro_id_rubro', blank=True, null=True)
    servicio_id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='servicio_id_servicio')
    comuna_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna_id_comuna', blank=True, null=True)
    cliente = models.CharField(max_length=200)
    profesional = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contrato_cliente'


class DetAccidente(models.Model):
    id_det_acc = models.FloatField(primary_key=True)
    descripcion_acc = models.CharField(max_length=1000, blank=True, null=True)
    accidente_id_accidente = models.ForeignKey(Accidente, models.DO_NOTHING, db_column='accidente_id_accidente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'det_accidente'


class DetalleVisita(models.Model):
    id_det_vis = models.FloatField(primary_key=True)
    visita_revision_id_vis_rev = models.ForeignKey('VisitaRevision', models.DO_NOTHING, db_column='visita_revision_id_vis_rev', blank=True, null=True)
    descripcion_vis = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'detalle_visita'


class Empleado(models.Model):
    id_empleado = models.FloatField(primary_key=True)
    nombre_emp = models.CharField(max_length=100)
    rut_emp = models.CharField(max_length=12)
    ap_materno_emp = models.CharField(max_length=100, blank=True, null=True)
    ap_paterno_emp = models.CharField(max_length=100, blank=True, null=True)
    grupo_cap_id_grupo_cap = models.ForeignKey('GrupoCap', models.DO_NOTHING, db_column='grupo_cap_id_grupo_cap')
    cliente = models.CharField(max_length=200)
    contrato_cliente_id_contrato = models.ForeignKey(ContratoCliente, models.DO_NOTHING, db_column='contrato_cliente_id_contrato', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class GrupoCap(models.Model):
    id_grupo_cap = models.FloatField(primary_key=True)
    capacitacion_id_capacitacion = models.ForeignKey(Capacitacion, models.DO_NOTHING, db_column='capacitacion_id_capacitacion')

    class Meta:
        managed = False
        db_table = 'grupo_cap'


class HistorialAcciones(models.Model):
    id_historial = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'historial_acciones'


class Pago(models.Model):
    id_pago = models.FloatField(primary_key=True)
    tipo_pago_id_tip_pago = models.ForeignKey('TipoPago', models.DO_NOTHING, db_column='tipo_pago_id_tip_pago')
    total_pago = models.BigIntegerField()
    fecha_pago = models.CharField(max_length=10)
    contrato_cliente_id_contrato = models.ForeignKey(ContratoCliente, models.DO_NOTHING, db_column='contrato_cliente_id_contrato', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pago'


class Region(models.Model):
    id_region = models.FloatField(primary_key=True)
    nombre_region = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'region'


class Rubro(models.Model):
    id_rubro = models.FloatField(primary_key=True)
    nombre_rub = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'rubro'


class Servicio(models.Model):
    id_servicio = models.FloatField(primary_key=True)
    nombre_serv = models.CharField(max_length=200)
    valor_serv = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'servicio'


class ServicioExtra(models.Model):
    servicio_id_servicio = models.ForeignKey(Servicio, models.DO_NOTHING, db_column='servicio_id_servicio', blank=True, null=True)
    id_serv_ex = models.FloatField(primary_key=True)
    nombre_serv_ex = models.CharField(max_length=200)
    valor_serv_ex = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'servicio_extra'


class TipoAccidente(models.Model):
    id_tipo_acc = models.FloatField(primary_key=True)
    nombre_tipo_acc = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'tipo_accidente'


class TipoPago(models.Model):
    id_tip_pago = models.FloatField(primary_key=True)
    nombre_tipo_pago = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'tipo_pago'


class VisitaRevision(models.Model):
    id_vis_rev = models.FloatField(primary_key=True)
    fecha_visita = models.CharField(max_length=10)
    contrato_cliente_id_contrato = models.ForeignKey(ContratoCliente, models.DO_NOTHING, db_column='contrato_cliente_id_contrato')

    class Meta:
        managed = False
        db_table = 'visita_revision'
