# Generated by Django 3.2.5 on 2021-10-10 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0048_alter_typeproduit_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.typeproduit'),
        ),
    ]
