# Generated by Django 3.2.5 on 2021-11-19 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0078_alter_prospect_langue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='fax',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='typeproduit',
            name='delete',
            field=models.BooleanField(),
        ),
    ]
