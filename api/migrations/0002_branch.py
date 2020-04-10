# Generated by Django 3.0.3 on 2020-04-09 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=50)),
                ('total_theater', models.IntegerField()),
            ],
        ),
    ]