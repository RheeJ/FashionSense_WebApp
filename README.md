# FashionSense WebApp

## Description
A webapp that hosts our awesome endpoints.


## Install
* [install Docker](https://docs.docker.com/engine/installation/)

## Usage
* to run with Docker
    * first build everything with Docker
    ```
    $ docker build -t api
    ```
    * to run with Docker
    ```
    $ docker run -p 8080:8080 api .
    ```

* alternatively run it locally just using Django
    * first cd into the api directories
    * do migrations
    ```
    $ python manage.py migrate
    ```
    * now to start the app on localhost:8080 run
    ```
    $ python manage.py runserver
    ```
