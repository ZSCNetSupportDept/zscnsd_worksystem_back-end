# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-08 18:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buff',
            name='key',
        ),
        migrations.DeleteModel(
            name='Buff',
        ),
    ]