# Generated by Django 3.0.5 on 2020-04-25 21:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200424_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='supply_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='공급일자'),
        ),
    ]