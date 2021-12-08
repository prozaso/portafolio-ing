# Generated by Django 3.2.7 on 2021-10-12 05:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telefono',
            field=models.CharField(max_length=12, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
    ]
