# Generated by Django 3.2.5 on 2021-10-05 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0037_pays_delete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ville',
            name='pays',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.pays'),
        ),
    ]
