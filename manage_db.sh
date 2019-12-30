#!/bin/bash
python manage_db.py db init
python manage_db.py db migrate
python manage_db.py db upgrade
