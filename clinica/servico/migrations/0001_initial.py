# Generated by Django 5.2.3 on 2025-07-13 11:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profissional', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.TextField(max_length=100)),
                ('imagem', models.FileField(upload_to='img_servico')),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servico', models.TextField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='preco')),
                ('arquivo', models.FileField(upload_to='img')),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profissional.profissional')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tiposServicos', to='servico.tiposervico')),
            ],
        ),
    ]
