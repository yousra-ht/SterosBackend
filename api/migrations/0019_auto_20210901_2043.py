# Generated by Django 3.2.5 on 2021-09-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_alter_action_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='contents',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='endtime',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='place',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
