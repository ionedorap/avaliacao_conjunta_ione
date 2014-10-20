# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_aluguel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
                ('Preco', models.FloatField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='filme',
            name='Categoria_Filme',
            field=models.ForeignKey(verbose_name=b'Categoria', to='cadastro.Categoria', null=True),
            preserve_default=True,
        ),
    ]
