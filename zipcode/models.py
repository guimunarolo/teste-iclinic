# -*- coding: utf-8 -*-

from django.db import models


class Zipcode(models.Model):

    class Meta:
        verbose_name = 'Zipcode'
        verbose_name_plural = 'Zipcodes'
        ordering = ['insertion', 'street']

    zipcode = models.CharField(u'CEP', max_length=8)
    street = models.CharField(u'Logradouro', max_length=255)
    neighborhood = models.CharField(u'Bairro', max_length=255)
    city = models.CharField(u'Cidade', max_length=255)
    state = models.CharField(u'Estado', max_length=255)
    insertion = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.zipcode
