# Generated by Django 3.2.5 on 2021-11-11 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0067_auto_20211111_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='type',
            field=models.ForeignKey(default='4', on_delete=django.db.models.deletion.CASCADE, to='api.typeproduit'),
        ),
    ]
