# Generated by Django 2.2.17 on 2021-02-19 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_failedlogin_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='failedlogin',
            name='user',
        ),
    ]
