# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20160324_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powder',
            name='price_retail',
            field=models.FloatField(verbose_name='\u0426\u0435\u043d\u0430 \u0440\u043e\u0437\u043d\u0438\u0446\u0430'),
        ),
        migrations.DeleteModel(
            name='Retail',
        ),
        migrations.AlterField(
            model_name='powder',
            name='price_wholesale',
            field=models.FloatField(verbose_name='\u0426\u0435\u043d\u0430 \u043e\u043f\u0442.'),
        ),
        migrations.DeleteModel(
            name='Wholesale',
        ),
    ]
