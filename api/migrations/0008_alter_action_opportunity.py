# Generated by Django 3.2.5 on 2021-08-27 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210827_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='Opportunity',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.opportunities'),
        ),
    ]