# Generated by Django 3.0.5 on 2020-06-10 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_delivery', '0006_auto_20200609_2314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='usuario',
        ),
    ]