# Generated by Django 3.2.5 on 2021-11-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0081_alter_ville_ville'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Tel',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='prospect',
            name='Tel',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
