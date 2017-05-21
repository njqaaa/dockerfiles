#!/bin/bash
cd /root/jumpserver
python3 apps/manage.py makemigrations
python3 apps/manage.py migrate
python3 apps/manage.py loaddata init
