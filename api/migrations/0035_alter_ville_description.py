# Generated by Django 3.2.5 on 2021-10-05 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_ville_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ville',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
