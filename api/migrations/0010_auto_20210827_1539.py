# Generated by Django 3.2.5 on 2021-08-27 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_action_enddate'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='contents',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='duration',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='place',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
