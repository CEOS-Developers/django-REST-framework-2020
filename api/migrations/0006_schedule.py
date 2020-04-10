# Generated by Django 3.0.3 on 2020-04-09 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_date', models.DateField()),
                ('schedule_time', models.TimeField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Branch')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Movie')),
                ('theater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Theater')),
            ],
        ),
    ]