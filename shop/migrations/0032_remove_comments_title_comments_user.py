# Generated by Django 4.0.2 on 2022-04-03 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0012_alter_user_number'),
        ('shop', '0031_remove_comments_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='title',
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users_api.user'),
        ),
    ]
