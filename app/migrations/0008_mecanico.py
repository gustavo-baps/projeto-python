# Generated by Django 4.2.6 on 2023-11-15 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_delete_mecanico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mecanico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45, unique=True)),
                ('sobrenome', models.CharField(max_length=45)),
                ('endereco', models.CharField(max_length=100, unique=True)),
                ('especialidade', models.CharField(max_length=100)),
                ('equipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.equipe')),
            ],
        ),
    ]
