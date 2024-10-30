# Generated by Django 5.1 on 2024-10-25 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_financeiro_data_de_pagamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='financeiro',
            name='codigo_receita',
            field=models.CharField(default='1708', max_length=4),
        ),
        migrations.AddField(
            model_name='financeiro',
            name='data_vencimento',
            field=models.DateField(default=datetime.datetime(2024, 10, 25, 13, 36, 43, 54267, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='financeiro',
            name='periodo_apuracao',
            field=models.DateField(default=datetime.datetime(2024, 10, 25, 13, 36, 58, 577067, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]