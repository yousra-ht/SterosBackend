# Generated by Django 3.2.5 on 2022-02-08 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0083_alter_ville_ville'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ville',
            name='adresse',
        ),
    ]