# Generated by Django 3.0.10 on 2023-06-26 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TaskTamer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='date_create',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='username',
        ),
        migrations.RemoveField(
            model_name='rewards',
            name='tasks',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='users',
        ),
        migrations.RemoveField(
            model_name='user_tasks',
            name='users_tasks',
        ),
        migrations.AddField(
            model_name='user_tasks',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TaskTamer.Tasks'),
        ),
        migrations.AddField(
            model_name='user_tasks',
            name='task_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user_tasks',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rewards',
            name='rewards_cost',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Acivement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rewards', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TaskTamer.Rewards')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
