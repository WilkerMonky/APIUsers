# Generated by Django 4.2 on 2023-10-24 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastroUser', '0003_remove_usuariocomum_nome_completo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuariocomum',
            name='ativo',
        ),
    ]