# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Powder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=225)),
                ('powder_type', models.CharField(max_length=255, choices=[(1, '\u0414\u043b\u044f \u0446\u0432\u0435\u0442\u043d\u043e\u0433\u043e \u0431\u0435\u043b\u044c\u044f'), (2, '\u0414\u043b\u044f \u0431\u0435\u043b\u043e\u0433\u043e \u0431\u0435\u043b\u044c\u044f')])),
                ('packing', models.IntegerField(choices=[(3, b'3kg'), (15, b'15kg')])),
                ('price_wholesale', models.FloatField(verbose_name='\u0426\u0435\u043d\u0430 \u043e\u043f\u0442.')),
                ('price_retail', models.FloatField(verbose_name='\u0426\u0435\u043d\u0430 \u0440\u043e\u0437\u043d\u0438\u0446\u0430')),
                ('description', models.TextField()),
                ('photo', models.ImageField(null=True, upload_to=b'products_img')),
                ('availability', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
