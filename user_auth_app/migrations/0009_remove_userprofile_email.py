# Generated by Django 5.1.2 on 2024-12-15 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth_app', '0008_alter_userprofile_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]
