# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-31 15:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_rent', '0003_auto_20180331_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movierent',
            old_name='rent_by',
            new_name='created_by',
        ),
    ]
