# Generated by Django 3.2.5 on 2021-11-11 22:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0075_alter_opportunities_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='Contact',
            field=models.ManyToManyField(to='api.Contact'),
        ),
        migrations.AlterField(
            model_name='action',
            name='Opportunity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.opportunities'),
        ),
        migrations.AlterField(
            model_name='action',
            name='endDate',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='action',
            name='status',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='action',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.newuser'),
        ),
    ]
