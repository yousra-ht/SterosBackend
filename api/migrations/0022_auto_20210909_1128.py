# Generated by Django 3.2.5 on 2021-09-09 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_contact_function'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='endtime',
        ),
        migrations.RemoveField(
            model_name='action',
            name='starttime',
        ),
        migrations.AddField(
            model_name='action',
            name='endDate',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
