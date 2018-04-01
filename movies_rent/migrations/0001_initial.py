# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-31 13:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies_catalog', '0002_movie_rent_amt'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('rent_at', models.DateTimeField(auto_now_add=True)),
                ('rent_start_date', models.DateField()),
                ('rent_end_date', models.DateField()),
                ('rent_total_days', models.IntegerField()),
                ('rent_amt', models.DecimalField(decimal_places=2, max_digits=19)),
                ('penalty_amt', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('total_amt', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('status', models.CharField(max_length=2)),
                ('returned_at', models.DateTimeField()),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies_catalog.Movie')),
                ('rent_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rent_by', to=settings.AUTH_USER_MODEL)),
                ('returned_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='returned_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
