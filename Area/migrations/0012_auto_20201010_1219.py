# Generated by Django 3.1.1 on 2020-10-10 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Area', '0011_areaclass_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areaclass',
            name='area_image',
            field=models.ImageField(blank=True, default='AreaPic/images/default.jpg', upload_to='AreaPic/images'),
        ),
    ]