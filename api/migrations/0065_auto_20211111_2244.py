# Generated by Django 3.2.5 on 2021-11-11 21:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0064_alter_produit_prix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Ville',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='api.ville'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='adresse',
            field=models.CharField(default='adresse', max_length=150),
        ),
        migrations.AlterField(
            model_name='contact',
            name='birthday',
            field=models.CharField(default='12/04/1998', max_length=150),
        ),
        migrations.AlterField(
            model_name='contact',
            name='delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='function',
            field=models.CharField(default='function', max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='lastname',
            field=models.CharField(default='lastname', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='pays',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='api.pays'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='prospect',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='api.prospect'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]