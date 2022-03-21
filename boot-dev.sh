#!/bin/bash

cd /app
echo "Installing challenge package for live development.."
pip install -e .

echo "Starting server.."
export FLASK_APP=manage.py
export FLASK_ENV=development

python manage.py db upgrade
python manage.py movielens seed-data
flask run --host=0.0.0.0 --port=80
