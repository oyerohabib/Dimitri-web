# Generated by Django 3.1.4 on 2021-02-08 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210208_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='Hire_Date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='driver',
            name='Term_Date',
            field=models.DateTimeField(),
        ),
    ]
