# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-07 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100, null=True)),
                ('type_code', models.CharField(max_length=100, null=True)),
                ('image_url', models.CharField(max_length=200, null=True)),
                ('local_url', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]