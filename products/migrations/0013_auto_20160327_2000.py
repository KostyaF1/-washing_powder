# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20160327_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powder',
            name='packing',
            field=models.CharField(max_length=2, choices=[(b'3kg', b'3'), (b'3kg', b'15')]),
        ),
        migrations.AlterField(
            model_name='powder',
            name='powder_type',
            field=models.CharField(max_length=1, choices=[(b'\xd0\x94\xd0\xbb\xd1\x8f \xd0\xa6\xd0\xb2\xd0\xb5\xd1\x82\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\x91\xd0\xb5\xd0\xbb\xd1\x8c\xd1\x8f', b'C'), (b'\xd0\x94\xd0\xbb\xd1\x8f \xd0\x91\xd0\xb5\xd0\xbb\xd0\xbe\xd0\xb3\xd0\xbe \xd0\x91\xd0\xb5\xd0\xbb\xd1\x8c\xd1\x8f', b'W')]),
        ),
    ]
