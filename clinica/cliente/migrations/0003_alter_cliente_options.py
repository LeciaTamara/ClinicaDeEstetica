# Generated by Django 4.2.11 on 2025-07-14 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_agendarservico'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'permissions': (('detail_cliente', 'Pode ver detalhe do perfil'), ('AgendarServico_cliente', 'Pode agendar um servico'))},
        ),
    ]
