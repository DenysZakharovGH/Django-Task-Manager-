# Generated by Django 2.2.1 on 2019-05-01 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_task_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('inp', 'in process'), ('d', 'done'), ('rj', 'reject')], default='new', max_length=3),
        ),
    ]
