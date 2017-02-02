#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn --reload fashionsense.wsgi:application \
    --bind 0.0.0.0:8080
