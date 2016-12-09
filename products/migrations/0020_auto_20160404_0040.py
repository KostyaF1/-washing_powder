# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_powder_propose'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='powder',
            name='propose',
        ),
        migrations.AddField(
            model_name='aboutpowder',
            name='propose',
            field=models.TextField(default=b'Malve'),
            preserve_default=True,
        ),
    ]
