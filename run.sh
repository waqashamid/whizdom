#!/bin/bash
python manage.py makemigrations
python manage.py migrate --noinput
django-admin --settings=whizdom.settings
python manage.py check
python manage.py createsu
python manage.py runserver 5000
