# Generated by Django 3.1.1 on 2020-10-09 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Member', '0015_auto_20201010_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberclass',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='memberclass',
            name='status',
        ),
        migrations.RemoveField(
            model_name='memberclass',
            name='updated_date',
        ),
        migrations.AlterField(
            model_name='memberclass',
            name='interest_in',
            field=models.CharField(choices=[('Volunteer', 'Volunteer'), ('Donor', 'Donor')], default='Null', max_length=30),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Completed', 'Completed')], default='Pending', max_length=30)),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Member.memberclass')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
