# Generated by Django 4.2.4 on 2023-08-28 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_rename_data_fotografia_usuarios_data_cadastro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuarios',
            old_name='senha',
            new_name='senha_usuario',
        ),
    ]
