# Generated by Django 4.2.6 on 2023-11-15 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_servico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='equipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.equipe'),
        ),
        migrations.AlterField(
            model_name='mecanico',
            name='equipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.equipe'),
        ),
        migrations.CreateModel(
            name='Ordem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('dataconclusao', models.DateField()),
                ('carro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.carro')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.cliente')),
                ('equipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.equipe')),
                ('servicos', models.ManyToManyField(to='app.servico')),
            ],
        ),
    ]