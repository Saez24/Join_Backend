# Generated by Django 5.1.2 on 2024-12-11 08:57

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth_app', '0002_remove_userprofile_bio_remove_userprofile_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default=None, max_length=100, verbose_name=django.contrib.auth.models.User),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='privacyCheckBox',
            field=models.BooleanField(default=False, verbose_name=django.contrib.auth.models.User),
        ),
    ]