# Generated by Django 5.0.4 on 2024-07-24 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nbs', '0002_bioficinadetalhado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('NUMERO_OS', models.IntegerField(primary_key=True, serialize=False)),
                ('COD_EMPRESA', models.IntegerField()),
                ('COD_SERVICO', models.IntegerField()),
                ('COD_TECNICO', models.IntegerField()),
                ('ITEM', models.CharField(max_length=100)),
                ('DATA_ENTRADA', models.DateField()),
                ('HORA_ENTRADA', models.TimeField()),
                ('TEMPO_PAGO', models.DecimalField(decimal_places=2, max_digits=5)),
                ('DATA_SAIDA', models.DateField()),
                ('HORA_SAIDA', models.TimeField()),
            ],
        ),
    ]
