# Generated by Django 3.0.5 on 2020-06-12 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_delivery', '0010_auto_20200611_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Esperando Restaurante'), (2, 'Em Produção'), (3, 'Saiu para Entrega')], default=1),
        ),
    ]
