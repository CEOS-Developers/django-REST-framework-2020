# Generated by Django 3.0.3 on 2020-04-14 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_pay'),
    ]

    operations = [
        migrations.RenameField('ReservationTicket', 'member', 'user'),
    ]