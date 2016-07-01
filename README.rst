=============
Teste iClinic
=============

Author: Guilherme Munarolo

Features
========
* Python 2.7
* Django 1.7.11
* Coverage 89%

How to run?
===========

Install dependences:

.. code:: sh

    $ pip install -r requirements.txt


Migrate:

.. code:: sh

    $ python manage.py migrate


Run:

.. code:: sh

    $ python manage.py runserver 0:8000


Requests:
=========

Inlcusion:

.. code:: sh

    $ curl --data '{"zip_code": "14020260"}' http://localhost:8000/zipcode/


List:

.. code:: sh

    $ curl http://localhost:8000/zipcode/


Exclusion:

.. code:: sh

    $ curl -X DELETE http://localhost:8000/zipcode/14020260/


Detail:

.. code:: sh

    $ curl http://localhost:8000/zipcode/14020260/