# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-24 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Extorsion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('phone', models.IntegerField()),
                ('description', models.TextField()),
                ('state', models.CharField(choices=[('IN', 'Interno'), ('EX', 'Externo')], max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
