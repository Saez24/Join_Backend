# Generated by Django 5.1.2 on 2024-11-03 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_app', '0006_alter_taskstatus_options_alter_names_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='subtask',
            field=models.ManyToManyField(blank=True, related_name='tasks', to='join_app.subtasks'),
        ),
    ]
