# Generated by Django 3.2.7 on 2021-10-09 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='razon_social',
            field=models.CharField(default=None, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='rut',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
    ]