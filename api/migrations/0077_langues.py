# Generated by Django 3.2.5 on 2021-11-19 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0076_auto_20211111_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Langues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('langue', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('delete', models.BooleanField()),
            ],
        ),
    ]