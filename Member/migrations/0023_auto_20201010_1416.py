# Generated by Django 3.1.1 on 2020-10-10 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0022_auto_20201010_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberclass',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/MembersPic/images'),
        ),
    ]
