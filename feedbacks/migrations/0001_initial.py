# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CallOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u0412\u0430\u0448\u0435 \u0438\u043c\u044f')),
                ('subject', models.CharField(max_length=100, verbose_name='\u0442\u0435\u043c\u0430')),
                ('phone', models.IntegerField(max_length=100, verbose_name='\u0412\u0430\u0448 \u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CompanyContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_1', models.IntegerField(max_length=100)),
                ('phone_2', models.IntegerField(max_length=100, null=True, blank=True)),
                ('email', models.EmailField(max_length=75)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=225, verbose_name='\u0412\u0430\u0448\u0435 \u0438\u043c\u044f')),
                ('subject', models.CharField(max_length=255, verbose_name='\u0442\u0435\u043c\u0430')),
                ('message', models.TextField(verbose_name='\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435')),
                ('from_email', models.EmailField(max_length=75)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
