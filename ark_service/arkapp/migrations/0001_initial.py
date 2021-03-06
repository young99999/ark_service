# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 06:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=25, unique=True)),
                ('date_created', models.DateField(auto_now=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Minter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('prefix', models.CharField(max_length=7, null=True)),
                ('template', models.CharField(max_length=25)),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='ark',
            name='minter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arkapp.Minter'),
        ),
    ]
