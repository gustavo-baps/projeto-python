# Generated by Django 4.2.6 on 2023-12-03 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_ordem_concluida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carro',
            name='equipe',
        ),
    ]
