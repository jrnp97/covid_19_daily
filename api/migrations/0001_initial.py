# Generated by Django 3.0.3 on 2020-03-21 05:06

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_file', models.FileField(upload_to='covid_data')),
                ('signature', models.TextField(unique=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('processed', models.BooleanField(default=False)),
                ('normalized', models.BooleanField(default=False)),
                ('process_detail', models.TextField(null=True)),
                ('headers', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_state', models.CharField(max_length=200, verbose_name='Province/State')),
                ('country_region', models.CharField(max_length=200, verbose_name='Country/Region')),
                ('last_update', models.DateTimeField(verbose_name='Last Update')),
                ('confirmed', models.BigIntegerField()),
                ('deaths', models.BigIntegerField()),
                ('recovered', models.BigIntegerField()),
                ('Suspected', models.BigIntegerField(blank=True, null=True)),
                ('latitude', models.BigIntegerField(blank=True, null=True)),
                ('longitude', models.BigIntegerField(blank=True, null=True)),
                ('report_day', models.DateField()),
            ],
        ),
    ]
