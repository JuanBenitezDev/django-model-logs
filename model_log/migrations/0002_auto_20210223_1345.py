# Generated by Django 3.1.7 on 2021-02-23 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model_log', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='object',
            new_name='model',
        ),
        migrations.RemoveField(
            model_name='log',
            name='user',
        ),
    ]
