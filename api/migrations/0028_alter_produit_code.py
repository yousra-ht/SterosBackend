# Generated by Django 3.2.5 on 2021-10-05 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20211005_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='code',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
