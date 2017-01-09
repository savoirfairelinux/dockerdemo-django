dockerdemo-django
#################

Super simple Django project featuring the use of Django with Docker...

Development setup
=================

First build the images:

.. code-block:: shell

  docker-compose build

Start the services (Gunicorn, Nginx, PostgreSQL and Redis):

.. code-block:: shell

  docker-compose up -d

Run the Django migrations:

.. code-block:: shell

  docker-compose run web /usr/local/bin/python manage.py migrate

Then go to http://localhost.

Production setup
================

Let's Deploy to an Azure VM using similar commands:

.. code-block:: shell

  docker-machine create -d azure --azure-ssh-user ops --azure-subscription-id [YOUR-SID-HERE] --azure-open-port 80 mytest
  eval "$(docker-machine env mytest)"
  docker-compose -f docker-compose.yml -f docker-compose.prod.yml build
  docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
  docker-compose -f docker-compose.yml -f docker-compose.prod.yml run web /usr/local/bin/python manage.py migrate

Retrieve the IP address of the machine using:

.. code-block:: shell

  docker-machine ip mytest

And then view it into your browser.
