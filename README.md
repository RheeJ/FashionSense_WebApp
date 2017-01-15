# FashionSense WebApp

## Description
A webapp that hosts our awesome endpoints


# Install
* [install Docker](https://docs.docker.com/engine/installation/)
* [install Docker Compose](https://docs.docker.com/compose/install/)

# Usage
* to run with Docker Compose
    * first build everything with Docker Compose
    ```
    $ docker-compose build
    ```
    * to run with Docker Compose
    ```
    $ docker-compose up
    ```

* alternatively run it locally just using Django
    * first cd into the api directories
    * do migrations
    ```
    $ python manage.py migrate
    ```
    * now to start the app on localhost:8000 run
    ```
    python manage.py runserver.
    ```
* now you can access the api by sending a post request to this endpoint -> [host]/api/classification (if you're on Mac Docker doesn't bind to localhost I think...)
