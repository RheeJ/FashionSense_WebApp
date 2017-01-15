#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn fashionsense.wsgi:application \
    --bind 0.0.0.0:8080