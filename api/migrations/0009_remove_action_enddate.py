# Generated by Django 3.2.5 on 2021-08-27 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_action_opportunity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='endDate',
        ),
    ]
