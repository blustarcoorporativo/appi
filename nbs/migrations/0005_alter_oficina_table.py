# Generated by Django 5.0.4 on 2024-07-25 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nbs', '0004_oficina_servico_alter_oficina_options'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='oficina',
            table='OS_TEMPOS_EXECUTADOS',
        ),
    ]
