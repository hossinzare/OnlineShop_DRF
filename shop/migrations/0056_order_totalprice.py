# Generated by Django 4.0.2 on 2022-04-27 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0055_alter_product_category_alter_product_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='totalPrice',
            field=models.IntegerField(null=True),
        ),
    ]
