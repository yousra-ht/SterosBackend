# Generated by Django 3.2.5 on 2021-10-10 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0046_typeproduit'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeproduit',
            name='delete',
            field=models.BooleanField(null=True),
        ),
    ]
