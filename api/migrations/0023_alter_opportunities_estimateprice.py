# Generated by Django 3.2.5 on 2021-09-10 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20210909_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunities',
            name='estimatePrice',
            field=models.FloatField(),
        ),
    ]