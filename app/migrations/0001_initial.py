# Generated by Django 3.2.7 on 2021-09-16 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accidente',
            fields=[
                ('id_accidente', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fecha_acc', models.CharField(max_length=10)),
                ('alerta', models.FloatField()),
            ],
            options={
                'db_table': 'accidente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id_admin', models.FloatField(primary_key=True, serialize=False)),
                ('nombre_adm', models.CharField(max_length=100)),
                ('rut_adm', models.CharField(max_length=12)),
                ('ap_materno_adm', models.CharField(max_length=100)),
                ('ap_paterno_adm', models.CharField(max_length=100)),
                ('fecha_nac_adm', models.CharField(blank=True, max_length=10, null=True)),
                ('telefono_adm', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion_adm', models.CharField(blank=True, max_length=300, null=True)),
                ('email_adm', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'administrador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AlertaCumplimiento',
            fields=[
                ('id_alerta_cum', models.FloatField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'alerta_cumplimiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('codename', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=254, null=True)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Capacitacion',
            fields=[
                ('id_capacitacion', models.FloatField(primary_key=True, serialize=False)),
                ('nombre_cap', models.CharField(max_length=100)),
                ('fecha_cap', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'capacitacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.FloatField(primary_key=True, serialize=False)),
                ('nombre_cli', models.CharField(max_length=300)),
                ('direccion_cli', models.CharField(max_length=300)),
                ('rut_cli', models.CharField(max_length=12)),
                ('telefono_cli', models.CharField(max_length=15)),
                ('correo_cli', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.FloatField(primary_key=True, serialize=False)),
                ('nombre_comuna', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'comuna',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Condicion',
            fields=[
                ('id_condicion', models.FloatField(primary_key=True, serialize=False)),
                ('nombre_condicion', models.CharField(blank=True, max_length=200, null=True)),
                ('detalle_condicion', models.CharField(max_length=1000)),
                ('valor_condicion', models.BigIntegerField()),
            ],
            options={
                'db_table': 'condicion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetAccidente',
            fields=[
                ('id_det_acc', models.FloatField(primary_key=True, serialize=False)),
                ('descripcion_acc', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'det_accidente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleVisita',
            fields=[
                ('id_det_vis', models.FloatField(primary_key=True, serialize=False)),
                ('descripcion_vis', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'detalle_visita',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(blank=True, max_length=200, null=True)),
                ('action_flag', models.IntegerField()),
                ('change_message', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField(blank=True, null=True)),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.FloatField(primary_key=True, serialize=False)),
                ('nombre_emp', models.CharField(max_length=100)),
                ('rut_emp', models.CharField(max_length=12)),
                ('ap_materno_emp', models.CharField(blank=True, max_length=100, null=True)),
                ('ap_paterno_emp', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GrupoCap',
            fields=[
                ('id_grupo_cap', models.FloatField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'grupo_cap',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HistorialAcciones',
            fields=[
                ('id_historial', models.FloatField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'historial_acciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.FloatField(primary_key=True, serialize=False)),
                ('total_pago', models.BigIntegerField()),
                ('fecha_pago', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'pago',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id_profesional', models.FloatField(primary_key=True, serialize=False)),
                ('nombre_pro', models.CharField(max_length=100)),
                ('rut_pro', models.CharField(max_length=12)),
                ('ap_materno_pro', models.CharField(max_length=100)),
                ('ap_paterno_pro', models.CharField(max_length=100)),
                ('fecha_nac_pro', models.CharField(blank=True, max_length=10, null=True)),
                ('telefono_pro', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion_pro', models.CharField(blank=True, max_length=200, null=True)),
                ('email_pro', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'profesional',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.FloatField(primary_key=True, serialize=False)),
                ('nombre_region', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id_rubro', models.FloatField(primary_key=True, serialize=False)),
                ('nombre_rub', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'rubro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_servicio', models.FloatField(primary_key=True, serialize=False)),
                ('nombre_serv', models.CharField(max_length=200)),
                ('valor_serv', models.BigIntegerField()),
            ],
            options={
                'db_table': 'servicio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServicioExtra',
            fields=[
                ('id_serv_ex', models.FloatField(primary_key=True, serialize=False)),
                ('nombre_serv_ex', models.CharField(max_length=200)),
                ('valor_serv_ex', models.BigIntegerField()),
            ],
            options={
                'db_table': 'servicio_extra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoAccidente',
            fields=[
                ('id_tipo_acc', models.FloatField(primary_key=True, serialize=False)),
                ('nombre_tipo_acc', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'tipo_accidente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id_tip_pago', models.FloatField(primary_key=True, serialize=False)),
                ('nombre_tipo_pago', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'tipo_pago',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VisitaRevision',
            fields=[
                ('id_vis_rev', models.FloatField(primary_key=True, serialize=False)),
                ('fecha_visita', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'visita_revision',
                'managed': False,
            },
        ),
    ]
