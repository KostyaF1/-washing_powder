# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20160324_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powderorder',
            name='name',
            field=models.ForeignKey(to='products.Powder'),
        ),
    ]
