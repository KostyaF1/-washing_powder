# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20160327_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powder',
            name='photo',
            field=models.ImageField(default=b'/images/pexels-photo-45718.jpeg', upload_to=b'powder'),
        ),
        migrations.AlterField(
            model_name='powder',
            name='powder_type',
            field=models.CharField(max_length=70, choices=[('\u0414\u043b\u044f \u0426\u0432\u0435\u0442\u043d\u043e\u0433\u043e \u0411\u0435\u043b\u044c\u044f', b'Color'), ('\u0414\u043b\u044f \u0411\u0435\u043b\u043e\u0433\u043e \u0411\u0435\u043b\u044c\u044f', b'White')]),
        ),
    ]
