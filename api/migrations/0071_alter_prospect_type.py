# Generated by Django 3.2.5 on 2021-11-11 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0070_auto_20211111_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='type',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
