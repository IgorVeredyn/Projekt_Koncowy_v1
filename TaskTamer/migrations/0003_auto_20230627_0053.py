# Generated by Django 3.0.10 on 2023-06-26 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskTamer', '0002_auto_20230626_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_tasks',
            name='date_complete',
        ),
        migrations.AlterField(
            model_name='tasks',
            name='task_description',
            field=models.CharField(max_length=200),
        ),
    ]
