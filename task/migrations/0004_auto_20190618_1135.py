# Generated by Django 2.2.1 on 2019-06-18 08:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20190617_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 6, 18, 11, 35, 28, 314741)),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
