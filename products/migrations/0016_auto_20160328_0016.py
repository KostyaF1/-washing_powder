# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20160327_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powder',
            name='photo',
            field=models.ImageField(default=b'/images/pexels-photo-45718.jpeg', upload_to=b'products'),
        ),
    ]
