# Generated by Django 3.2.5 on 2021-08-06 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='user_name',
        ),
        migrations.AddField(
            model_name='newuser',
            name='nom',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='newuser',
            name='prenom',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
