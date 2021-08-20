# Generated by Django 3.2.5 on 2021-08-18 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prospect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
                ('fax', models.CharField(max_length=150)),
                ('size', models.PositiveIntegerField()),
            ],
        ),
    ]
