# Generated by Django 3.2.5 on 2021-11-11 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0068_alter_produit_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.typeproduit'),
        ),
    ]
