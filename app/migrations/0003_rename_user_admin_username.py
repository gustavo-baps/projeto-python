# Generated by Django 4.2.6 on 2023-11-07 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cliente_rename_username_admin_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='user',
            new_name='username',
        ),
    ]
