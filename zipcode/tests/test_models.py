# -*- coding: utf-8 -*-

from django.test import TestCase

from .factories import ZipcodeFactory


class ZipCodeTest(TestCase):
    def setUp(self):
        self.zipcode = ZipcodeFactory()

    def test_01_unicode(self):
        self.assertEqual(unicode(self.zipcode), u'{0}'.format(self.zipcode.zipcode))
