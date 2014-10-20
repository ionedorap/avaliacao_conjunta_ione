# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_filme_genero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Data_Aluguel', models.DateField(null=True, verbose_name=b'Data do aluguel')),
                ('Data_Devolucao', models.DateField(null=True, verbose_name=b'Data devolu\xc3\xa7\xc3\xa3o')),
                ('Nome_Cliente', models.ForeignKey(verbose_name=b'Cliente', to='cadastro.Cliente')),
                ('Nome_Filme', models.ForeignKey(verbose_name=b'Filme', to='cadastro.Filme')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
