# Generated by Django 5.1.3 on 2024-12-14 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avtosalon', '0002_alter_car_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]