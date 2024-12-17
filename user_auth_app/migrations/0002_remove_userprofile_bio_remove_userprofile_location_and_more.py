# Generated by Django 5.1.2 on 2024-12-11 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='location',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='privacyCheckBox',
            field=models.BooleanField(default=False),
        ),
    ]
