# Generated by Django 3.2.5 on 2021-08-31 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_opportunities_creationdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunities',
            name='estimatePrice',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
    ]