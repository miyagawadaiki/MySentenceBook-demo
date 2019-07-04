#!/bin/sh
cd sentences
rm -d -r migrations/
cd ..
rm -d -r db.sqlite3
python manage.py makemigrations sentences
python manage.py migrate
python manage.py createsuperuser
