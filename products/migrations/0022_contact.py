# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_navbutton'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_1', models.IntegerField(max_length=15)),
                ('phone_2', models.IntegerField(max_length=15)),
                ('phone_3', models.IntegerField(max_length=15)),
                ('email', models.EmailField(max_length=75)),
                ('photo', models.ImageField(null=True, upload_to=b'products_img')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
