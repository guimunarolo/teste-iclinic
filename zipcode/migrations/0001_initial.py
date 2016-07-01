# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zipcode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zipcode', models.CharField(max_length=8, verbose_name='CEP')),
                ('street', models.CharField(max_length=255, verbose_name='Logradouro')),
                ('neighborhood', models.CharField(max_length=255, verbose_name='Bairro')),
                ('city', models.CharField(max_length=255, verbose_name='Cidade')),
                ('state', models.CharField(max_length=255, verbose_name='Estado')),
                ('insertion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['insertion', 'street'],
                'verbose_name': 'Zipcode',
                'verbose_name_plural': 'Zipcodes',
            },
            bases=(models.Model,),
        ),
    ]
