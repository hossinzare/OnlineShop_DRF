# Generated by Django 4.0.2 on 2022-02-07 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_crate_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='crate_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
