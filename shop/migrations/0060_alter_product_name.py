# Generated by Django 4.0.2 on 2022-04-29 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0059_alter_comments_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
