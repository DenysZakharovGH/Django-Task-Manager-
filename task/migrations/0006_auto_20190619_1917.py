# Generated by Django 2.2.1 on 2019-06-19 16:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_auto_20190618_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='check_list',
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 6, 19, 19, 17, 27, 618091)),
        ),
    ]