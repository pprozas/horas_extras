# Generated by Django 4.2.4 on 2023-08-29 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_horasextras'),
    ]

    operations = [
        migrations.AddField(
            model_name='horasextras',
            name='descricao_horas_extras',
            field=models.TextField(default=None),
        ),
    ]
