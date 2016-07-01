# -*- coding: utf-8 -*-

import factory

from zipcode.models import Zipcode


class ZipcodeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Zipcode

    city = factory.Sequence(lambda n: "%s" % n)
    zipcode = factory.Sequence(lambda n: "%08d" % n)
    street = factory.Sequence(lambda n: "%s" % n)
    state = factory.Sequence(lambda n: "%s" % n)
    neighborhood = factory.Sequence(lambda n: "%s" % n)
