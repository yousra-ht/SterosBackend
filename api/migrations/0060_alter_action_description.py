# Generated by Django 3.2.5 on 2021-10-14 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0059_auto_20211013_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
