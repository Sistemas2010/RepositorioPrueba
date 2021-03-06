# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=60)),
                ('apellidos', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
            ],
        ),
    ]
