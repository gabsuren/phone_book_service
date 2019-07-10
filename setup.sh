#!/bin/bash

# Install all necessary packages:
pip install requirements.txt

# Creates database folder and exports application path
mkdir DB
export FLASK_APP=main.py

# Creates a migration repository:
flask db init

# Generates an initial migration:
flask db migrate

# Apply the migration to the database:
flask db upgrade
