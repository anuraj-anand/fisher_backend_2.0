# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-26 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAndAccess_App', '0007_auto_20170326_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productqty',
            field=models.CharField(default=2, max_length=5),
            preserve_default=False,
        ),
    ]
