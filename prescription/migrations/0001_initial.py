# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-05-07 09:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('information', models.CharField(max_length=256)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('refills', models.IntegerField()),
                ('dosage', models.IntegerField()),
                ('unit', models.CharField(choices=[('g', 'grams'), ('mg', 'milligrams'), ('mcg', 'micrograms')], max_length=3)),
                ('removed', models.BooleanField(default=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Patient')),
            ],
        ),
    ]
