# Generated by Django 3.1.1 on 2020-09-23 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Area', '0004_auto_20200923_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='areaclass',
            name='volunteer_name',
        ),
    ]