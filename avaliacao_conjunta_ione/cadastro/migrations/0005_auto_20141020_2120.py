# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_auto_20141020_2056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluguel',
            old_name='Nome_Cliente',
            new_name='Nome_Client',
        ),
        migrations.RenameField(
            model_name='aluguel',
            old_name='Nome_Filme',
            new_name='Nome_Film',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='Nome',
            new_name='Nome_Cliente',
        ),
        migrations.RenameField(
            model_name='filme',
            old_name='Nome',
            new_name='Nome_Filme',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='Nome',
        ),
        migrations.AddField(
            model_name='categoria',
            name='Nome_Categoria',
            field=models.CharField(default='', max_length=100, verbose_name=b'Nome'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='filme',
            name='Quantidade',
            field=models.IntegerField(null=True, verbose_name=b'Quantidade'),
        ),
    ]
