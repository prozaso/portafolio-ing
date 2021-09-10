# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accidente(models.Model):
    id_accidente = models.BigIntegerField(primary_key=True)
    fecha_acc = models.CharField(max_length=10)
    id_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    alerta = models.FloatField()
    id_tipo_acc = models.ForeignKey('TipoAccidente', models.DO_NOTHING, db_column='id_tipo_acc', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accidente'


class Administrador(models.Model):
    id_admin = models.FloatField(primary_key=True)
    id_comuna = models.ForeignKey('Comuna', models.DO_NOTHING, db_column='id_comuna', blank=True, null=True)
    nombre_adm = models.CharField(max_length=100)
    rut_adm = models.CharField(max_length=12)
    ap_materno_adm = models.CharField(max_length=100)
    ap_paterno_adm = models.CharField(max_length=100)
    fecha_nac_adm = models.CharField(max_length=10, blank=True, null=True)
    telefono_adm = models.CharField(max_length=20, blank=True, null=True)
    direccion_adm = models.CharField(max_length=300, blank=True, null=True)
    email_adm = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'administrador'


class AlertaCumplimiento(models.Model):
    id_alerta_cum = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'alerta_cumplimiento'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Capacitacion(models.Model):
    id_capacitacion = models.FloatField(primary_key=True)
    id_profesional = models.ForeignKey('Profesional', models.DO_NOTHING, db_column='id_profesional', blank=True, null=True)
    id_admin = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='id_admin', blank=True, null=True)
    nombre_cap = models.CharField(max_length=100)
    fecha_cap = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'capacitacion'


class Cliente(models.Model):
    id_rubro = models.ForeignKey('Rubro', models.DO_NOTHING, db_column='id_rubro', blank=True, null=True)
    id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_servicio')
    id_cliente = models.FloatField(primary_key=True)
    id_comuna = models.ForeignKey('Comuna', models.DO_NOTHING, db_column='id_comuna', blank=True, null=True)
    id_admin = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='id_admin', blank=True, null=True)
    nombre_cli = models.CharField(max_length=300)
    direccion_cli = models.CharField(max_length=300)
    rut_cli = models.CharField(max_length=12)
    telefono_cli = models.CharField(max_length=15)
    correo_cli = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cliente'


class Comuna(models.Model):
    id_comuna = models.FloatField(primary_key=True)
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region')
    nombre_comuna = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'comuna'


class Condicion(models.Model):
    id_condicion = models.FloatField(primary_key=True)
    id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_servicio', blank=True, null=True)
    nombre_condicion = models.CharField(max_length=200, blank=True, null=True)
    detalle_condicion = models.CharField(max_length=1000)
    valor_condicion = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'condicion'


class DetAccidente(models.Model):
    id_det_acc = models.FloatField(primary_key=True)
    descripcion_acc = models.CharField(max_length=1000, blank=True, null=True)
    id_accidente = models.ForeignKey(Accidente, models.DO_NOTHING, db_column='id_accidente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'det_accidente'


class DetalleVisita(models.Model):
    id_det_vis = models.FloatField(primary_key=True)
    id_vis_rev = models.ForeignKey('VisitaRevision', models.DO_NOTHING, db_column='id_vis_rev', blank=True, null=True)
    descripcion_vis = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'detalle_visita'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    id_empleado = models.FloatField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    nombre_emp = models.CharField(max_length=100)
    rut_emp = models.CharField(max_length=12)
    ap_materno_emp = models.CharField(max_length=100, blank=True, null=True)
    ap_paterno_emp = models.CharField(max_length=100, blank=True, null=True)
    id_grupo_cap = models.ForeignKey('GrupoCap', models.DO_NOTHING, db_column='id_grupo_cap')

    class Meta:
        managed = False
        db_table = 'empleado'


class GrupoCap(models.Model):
    id_grupo_cap = models.FloatField(primary_key=True)
    id_capacitacion = models.ForeignKey(Capacitacion, models.DO_NOTHING, db_column='id_capacitacion')

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
    id_tip_pago = models.ForeignKey('TipoPago', models.DO_NOTHING, db_column='id_tip_pago')
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    total_pago = models.BigIntegerField()
    fecha_pago = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'pago'


class Profesional(models.Model):
    id_profesional = models.FloatField(primary_key=True)
    id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna', blank=True, null=True)
    nombre_pro = models.CharField(max_length=100)
    rut_pro = models.CharField(max_length=12)
    ap_materno_pro = models.CharField(max_length=100)
    ap_paterno_pro = models.CharField(max_length=100)
    fecha_nac_pro = models.CharField(max_length=10, blank=True, null=True)
    telefono_pro = models.CharField(max_length=20, blank=True, null=True)
    direccion_pro = models.CharField(max_length=200, blank=True, null=True)
    email_pro = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'profesional'


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
    id_servicio = models.ForeignKey(Servicio, models.DO_NOTHING, db_column='id_servicio', blank=True, null=True)
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
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_profesional = models.ForeignKey(Profesional, models.DO_NOTHING, db_column='id_profesional', blank=True, null=True)
    id_admin = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='id_admin')
    fecha_visita = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'visita_revision'
