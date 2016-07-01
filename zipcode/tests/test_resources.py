# -*- coding: utf-8 -*-

import factory

from django.test import TestCase

from .factories import ZipcodeFactory


class ZipCodeResourceTest(TestCase):
    def setUp(self):
        self.new_zipcode = ZipcodeFactory.create(
            city=u'Ribeirão Preto',
            zipcode='14025180',
            street=u'Rua São José',
            neighborhood=u'Jardim Sumaré',
            state=u'São Paulo',
        )

    def test_01_zipcode_list(self):
        response = self.client.get("/zipcode/")
        self.assertEqual(response.status_code, 200)

    def test_02_zipcode_detail(self):
        response = self.client.get("/zipcode/{}/".format(self.new_zipcode.zipcode))
        self.assertEqual(response.status_code, 200)

    def test_03_zipcode_create(self):
        response = self.client.post("/zipcode/", '{"zip_code": "14057140"}', content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_04_zipcode_delete(self):
        response = self.client.delete("/zipcode/14025180/")
        self.assertEqual(response.status_code, 204)

    def test_05_zipcode_not_found(self):
        response = self.client.delete("/zipcode/00000000/")
        self.assertEqual(response.status_code, 404)

    def test_06_zipcode_bad_request(self):
        response = self.client.get("/zipcode/1402178/")
        self.assertEqual(response.status_code, 400)
