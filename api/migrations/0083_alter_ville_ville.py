# Generated by Django 3.2.5 on 2022-02-07 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0082_auto_20211123_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ville',
            name='ville',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
