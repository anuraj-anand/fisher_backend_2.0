# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-26 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAndAccess_App', '0008_product_productqty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productqty',
            field=models.CharField(max_length=10),
        ),
    ]
