# Generated by Django 2.0.4 on 2018-04-21 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botify', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sessionevent',
            old_name='session_id',
            new_name='session',
        ),
    ]