# Generated by Django 3.1.1 on 2020-10-01 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donation', '0002_auto_20200921_1036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donationclass',
            old_name='donor_id',
            new_name='donor_name',
        ),
        migrations.RemoveField(
            model_name='donationclass',
            name='donation_id',
        ),
    ]
