# Generated by Django 3.2.5 on 2021-11-19 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0077_langues'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='langue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.langues'),
        ),
    ]