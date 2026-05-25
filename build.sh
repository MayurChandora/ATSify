#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Run migrations
python atsify_project/manage.py migrate

# Collect Static Files
python atsify_project/manage.py collectstatic --noinput
