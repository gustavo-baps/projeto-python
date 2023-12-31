# Generated by Django 4.2.6 on 2023-11-20 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_carro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defeito', models.CharField(max_length=255)),
                ('data', models.DateField()),
                ('dataconclusao', models.DateField()),
                ('carro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.carro')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.cliente')),
                ('equipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.equipe')),
                ('pecas', models.ManyToManyField(to='app.peca')),
                ('servicos', models.ManyToManyField(to='app.servico')),
            ],
        ),
    ]
