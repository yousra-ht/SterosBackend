# Generated by Django 3.2.5 on 2021-10-10 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0045_auto_20211010_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeProduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
