# Generated by Django 4.0.2 on 2022-04-03 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_alter_comments_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
    ]
