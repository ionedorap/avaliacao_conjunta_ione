# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_auto_20141020_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='Logradouro',
        ),
        migrations.RemoveField(
            model_name='filme',
            name='Quantidade',
        ),
        migrations.AddField(
            model_name='aluguel',
            name='Devolucao',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aluguel',
            name='Pagamento',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='Aluga',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aluguel',
            name='Nome_Client',
            field=models.ForeignKey(verbose_name=b'Cliente', to='cadastro.Cliente', null=True),
        ),
        migrations.AlterField(
            model_name='aluguel',
            name='Nome_Film',
            field=models.ForeignKey(verbose_name=b'Filme', to='cadastro.Filme', null=True),
        ),
        migrations.AlterField(
            model_name='filme',
            name='Categoria_Filme',
            field=models.ForeignKey(verbose_name=b'Categoria', to='cadastro.Categoria'),
        ),
    ]
