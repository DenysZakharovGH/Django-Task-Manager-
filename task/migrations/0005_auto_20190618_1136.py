# Generated by Django 2.2.1 on 2019-06-18 08:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20190618_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 6, 18, 11, 36, 23, 858067)),
        ),
    ]
