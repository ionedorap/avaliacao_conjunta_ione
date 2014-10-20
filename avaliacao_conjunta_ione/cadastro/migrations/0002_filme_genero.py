# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='Genero',
            field=models.CharField(max_length=10, null=True, choices=[(b'Terror', b'Terror'), (b'Comedia', b'Com\xc3\xa9dia'), (b'Acao', b'A\xc3\xa7\xc3\xa3o'), (b'Aventura', b'Aventura'), (b'Suspense', b'Suspense'), (b'Drama', b'Drama')]),
            preserve_default=True,
        ),
    ]
