# Generated by Django 3.2.5 on 2021-11-11 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0073_alter_opportunities_estimateprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunities',
            name='delete',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='opportunities',
            name='description',
            field=models.TextField(null=True),
        ),
    ]