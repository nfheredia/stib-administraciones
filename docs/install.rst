Install
=========


Migraciones
============
python manage.py migrate easy_thumbnails

python manage.py schemamigration allauth.account --initial
python manage.py migrate allauth.account

