# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20160327_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powder',
            name='packing',
            field=models.CharField(max_length=70, choices=[(b'3kg', b'3'), (b'15kg', b'15')]),
        ),
        migrations.AlterField(
            model_name='powder',
            name='powder_type',
            field=models.CharField(max_length=70, choices=[('\u0414\u043b\u044f \u0426\u0432\u0435\u0442\u043d\u043e\u0433\u043e \u0411\u0435\u043b\u044c\u044f', b'C'), ('\u0414\u043b\u044f \u0411\u0435\u043b\u043e\u0433\u043e \u0411\u0435\u043b\u044c\u044f', b'W')]),
        ),
    ]
