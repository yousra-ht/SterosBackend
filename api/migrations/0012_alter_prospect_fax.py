# Generated by Django 3.2.5 on 2021-08-31 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_action_endtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='fax',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
