# Generated by Django 4.2.23 on 2025-07-02 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escala', '0002_tipoatividade_sigla_complementar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoatividade',
            name='sigla',
            field=models.CharField(max_length=4),
        ),
    ]
