# Generated by Django 4.2.6 on 2023-11-15 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_equipe_mecanico_rename_username_admin_user_carro'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mecanico',
        ),
    ]
