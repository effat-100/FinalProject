# Generated by Django 3.1.1 on 2020-09-21 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0002_auto_20200921_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerclass',
            name='volunteer_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
