# Generated by Django 3.0.3 on 2020-04-23 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20200424_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='running_time',
        ),
    ]