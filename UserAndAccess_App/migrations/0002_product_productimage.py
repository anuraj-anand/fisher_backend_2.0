# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-25 00:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('UserAndAccess_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productImage',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=b''),
            preserve_default=False,
        ),
    ]
