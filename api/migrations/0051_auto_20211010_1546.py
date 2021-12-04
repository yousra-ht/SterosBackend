# Generated by Django 3.2.5 on 2021-10-10 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0050_alter_produit_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='type',
        ),
        migrations.AddField(
            model_name='produit',
            name='type1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.typeproduit'),
        ),
    ]