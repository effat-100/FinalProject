# Generated by Django 3.1.1 on 2020-10-10 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0020_auto_20201010_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberclass',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='MembersPic/images'),
        ),
    ]
