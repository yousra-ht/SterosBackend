# Generated by Django 3.2.5 on 2022-01-20 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0007_alter_newuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='delete',
            field=models.BooleanField(default=False),
        ),
    ]