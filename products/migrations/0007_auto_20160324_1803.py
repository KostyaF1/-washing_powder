# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20160324_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='PowderOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('powder_type', models.IntegerField(max_length=3, choices=[(1, b'\xd0\x94\xd0\xbb\xd1\x8f \xd1\x86\xd0\xb2\xd0\xb5\xd1\x82\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb1\xd0\xb5\xd0\xbb\xd1\x8c\xd1\x8f'), (2, b'\xd0\x94\xd0\xbb\xd1\x8f \xd0\xb1\xd0\xb5\xd0\xbb\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb1\xd0\xb5\xd0\xbb\xd1\x8c\xd1\x8f')])),
                ('packing', models.IntegerField(choices=[(3, b'3kg'), (15, b'15kg')])),
                ('price_wholesale', models.FloatField(verbose_name='\u0426\u0435\u043d\u0430 \u043e\u043f\u0442.')),
                ('price_retail', models.FloatField(verbose_name='\u0426\u0435\u043d\u0430 \u0440\u043e\u0437\u043d\u0438\u0446\u0430')),
                ('number', models.IntegerField(max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='powder',
            name='name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='powder',
            name='powder_type',
            field=models.IntegerField(max_length=3, choices=[(1, b'\xd0\x94\xd0\xbb\xd1\x8f \xd1\x86\xd0\xb2\xd0\xb5\xd1\x82\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb1\xd0\xb5\xd0\xbb\xd1\x8c\xd1\x8f'), (2, b'\xd0\x94\xd0\xbb\xd1\x8f \xd0\xb1\xd0\xb5\xd0\xbb\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb1\xd0\xb5\xd0\xbb\xd1\x8c\xd1\x8f')]),
        ),
    ]
