# Generated by Django 3.0.3 on 2020-04-11 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('name', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('total_seat', models.IntegerField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theaters', to='api.Branch')),
            ],
        ),
    ]