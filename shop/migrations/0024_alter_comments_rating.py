# Generated by Django 4.0.2 on 2022-04-01 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_comments_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='rating',
            field=models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')]),
        ),
    ]
