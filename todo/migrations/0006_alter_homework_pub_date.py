# Generated by Django 4.0.5 on 2022-07-03 15:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_alter_homework_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date Published'),
        ),
    ]
