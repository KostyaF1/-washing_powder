# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20160324_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powder',
            name='price_retail',
            field=models.ForeignKey(to='products.Retail'),
        ),
        migrations.AlterField(
            model_name='powder',
            name='price_wholesale',
            field=models.ForeignKey(to='products.Wholesale'),
        ),
    ]
