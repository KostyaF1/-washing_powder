# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20160324_0052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Retail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('packing', models.IntegerField(choices=[(3, b'3kg'), (15, b'15kg')])),
                ('price_retail', models.FloatField(verbose_name='\u0426\u0435\u043d\u0430 \u0440\u043e\u0437\u043d\u0438\u0446\u0430')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wholesale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('packing', models.IntegerField(choices=[(3, b'3kg'), (15, b'15kg')])),
                ('price_wholesale', models.FloatField(verbose_name='\u0426\u0435\u043d\u0430 \u043e\u043f\u0442.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='powder',
            name='price_retail',
            field=models.OneToOneField(to='products.Retail'),
        ),
        migrations.AlterField(
            model_name='powder',
            name='price_wholesale',
            field=models.OneToOneField(to='products.Wholesale'),
        ),
    ]
