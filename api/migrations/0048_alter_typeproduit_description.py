# Generated by Django 3.2.5 on 2021-10-10 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0047_typeproduit_delete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeproduit',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]