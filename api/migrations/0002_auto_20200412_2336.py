# Generated by Django 3.0.5 on 2020-04-12 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='std_major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Major'),
        ),
    ]