# Generated by Django 4.2.4 on 2023-08-18 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='empId',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.IntegerField(),
        ),
    ]