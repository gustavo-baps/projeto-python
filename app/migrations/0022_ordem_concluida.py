# Generated by Django 4.2.6 on 2023-12-03 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_ordem_totalvenda'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordem',
            name='concluida',
            field=models.BooleanField(default=False),
        ),
    ]
