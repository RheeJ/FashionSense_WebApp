# FashionSense_WebApp
Oh and Docker needs to be installed.
To run locally, cd into fashionsense then run:
"docker build -t [what you want to call it] ."
and
"docker run -p 8080:8080 [what you decided to call it]"


You can also run django app on localhost:8000 by cd'ing into folder with manage.py and running "python manage.py runserver."
But before that you will want to make sure your local database is updated by running "python manage.py makemigrations" and then "python manage.py migrate" To access python shell of your webapp, you can run "python manage.py shell"

