# Generated by Django 3.2.5 on 2021-09-01 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20210901_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='Contact',
            field=models.ManyToManyField(to='api.Contact'),
        ),
    ]