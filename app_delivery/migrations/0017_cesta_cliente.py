# Generated by Django 3.0.5 on 2020-06-13 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_delivery', '0016_remove_cesta_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='cesta',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_delivery.Cliente'),
        ),
    ]