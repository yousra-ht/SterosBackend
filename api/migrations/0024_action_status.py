# Generated by Django 3.2.5 on 2021-09-10 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_alter_opportunities_estimateprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='status',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
