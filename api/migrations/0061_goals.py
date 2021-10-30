# Generated by Django 3.2.5 on 2021-10-15 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0060_alter_action_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chiffre', models.CharField(max_length=150)),
                ('recouvrement', models.CharField(blank=True, max_length=150)),
                ('startDate', models.CharField(max_length=150)),
                ('endDate', models.CharField(blank=True, max_length=150)),
                ('objectif', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
