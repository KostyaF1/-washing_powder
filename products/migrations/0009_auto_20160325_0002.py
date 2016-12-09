# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20160324_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='powderorder',
            name='name',
        ),
        migrations.DeleteModel(
            name='PowderOrder',
        ),
    ]
