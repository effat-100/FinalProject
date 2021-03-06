# Generated by Django 3.1.1 on 2020-10-10 05:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Donation', '0005_auto_20201010_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationclass',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='donationclass',
            name='donation_options',
            field=models.CharField(choices=[('Bkash', 'Bkash'), ('Rocket', 'Rocket'), ('Donate by person', 'Donate by person')], default='Donate by person', max_length=50),
        ),
    ]
