# Generated by Django 3.0.10 on 2023-07-12 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskTamer', '0005_auto_20230712_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='chalenge_task_description',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='challenge_task_title',
        ),
        migrations.AddField(
            model_name='tasks',
            name='publik',
            field=models.BooleanField(default=False),
        ),
    ]