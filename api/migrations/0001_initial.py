# Generated by Django 3.0.5 on 2020-04-11 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=20, verbose_name='password')),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='email address')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='name')),
                ('phone', models.CharField(max_length=20, verbose_name='phone number')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('neither', 'neither')], default='male', max_length=10, verbose_name='gender')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('location', models.CharField(blank=True, max_length=100, verbose_name='location')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
