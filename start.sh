#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn --reload website.wsgi:application --bind 0.0.0.0:8080
