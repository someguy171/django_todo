# Generated by Django 4.0.5 on 2022-07-03 14:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_rename_name_homework_title_homework_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 7, 3, 14, 59, 37, 424988, tzinfo=utc), verbose_name='Date Published'),
        ),
    ]