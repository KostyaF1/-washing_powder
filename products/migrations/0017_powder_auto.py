# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20160328_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='powder',
            name='auto',
            field=models.CharField(default=b'no', max_length=70, choices=[('\u0410\u0432\u0442\u043e\u043c\u0430\u0442', b'yes'), ('\u0420\u0443\u0447\u043d\u0430\u044f \u0441\u0442\u0438\u0440\u043a\u0430', b'no')]),
            preserve_default=True,
        ),
    ]
