# Generated by Django 3.1.1 on 2020-10-07 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0010_auto_20201007_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberclass',
            name='image',
            field=models.ImageField(blank=True, default='MembersPic/images/default.jpg', upload_to='MembersPic/images/'),
        ),
    ]