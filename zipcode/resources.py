# -*- coding: utf-8 -*-

import logging
import requests

from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from restless.exceptions import BadRequest, NotFound

from .models import Zipcode


logger = logging.getLogger('zipcode.resources')


class ZipcodeResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        u'id': 'id',
        u'cep': 'zipcode',
        u'logradouro': 'street',
        u'bairro': 'neighborhood',
        u'cidade': 'city',
        u'estado': 'state',
        u'cadastro': 'insertion',
    })

    def get_zipcode(self, zipcode):
        logger.info(u'Trying to get zip code {} on database'.format(zipcode))
        return Zipcode.objects.get(zipcode=zipcode)

    def is_authenticated(self):
        return True

    def list(self):
        logger.info(u'Listing zip codes')
        limit = self.request.GET.get('limit')
        return Zipcode.objects.all()[:limit]

    def detail(self, zipcode):
        try:
            return self.get_zipcode(zipcode)
        except Zipcode.DoesNotExist:
            self.data['zip_code'] = zipcode
            return self.create()

    def create(self):
        zipcode = self.data['zip_code']

        try:
            return self.get_zipcode(zipcode)
        except Zipcode.DoesNotExist:
            logger.debug(u'Zip code {} does not exist on database.'.format(zipcode))
            logger.info(u'Trying to get zip code {} on postmon'.format(zipcode))

            request = requests.get('http://api.postmon.com.br/v1/cep/{}'.format(zipcode))

            if request.status_code == 200:
                logger.info(u'Created zip code {} with success'.format(zipcode))
                ret = request.json()
                return Zipcode.objects.create(
                    zipcode=ret['cep'],
                    street=ret['logradouro'],
                    neighborhood=ret['bairro'],
                    city=ret['cidade'],
                    state=ret['estado'],
                )
            else:
                logger.error(u'Invalid zip code {}. Required format: xxxxxxxx'.format(zipcode))
                raise BadRequest(msg='This zip code is invalid')

    def delete(self, zipcode):
        try:
            zipcode = self.get_zipcode(zipcode)
            logger.info(u'Removing zip code {} from database'.format(zipcode))
            zipcode.delete()
        except Zipcode.DoesNotExist:
            logger.debug(u'Zip code {} does not exist on database.'.format(zipcode))
            raise NotFound(msg='Zip code {} does not exist on database.'.format(zipcode))
