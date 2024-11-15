# Generated by Django 5.1.2 on 2024-11-02 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_app', '0003_remove_tasks_status_tasks_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='category',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='priority',
        ),
        migrations.AddField(
            model_name='tasks',
            name='category',
            field=models.CharField(choices=[('it', 'IT'), ('finance', 'Finance'), ('sales', 'Sales'), ('hr', 'HR'), ('marketing', 'Marketing'), ('operations', 'Operations')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tasks',
            name='priority',
            field=models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('urgent', 'Urgent')], default='medium', max_length=20),
        ),
    ]
