# FashionSense WebApp

## Description
A webapp that hosts our awesome endpoints


# Install
* install Docker

# Usage

* to run with Docker build and run the image

    ```
    $ docker build -t [what you want to call it] .; docker run -p 8080:8080 [what you decided to call it]
    ```

* alternatively run it locally just using Django
    * first setup migrations
    ```
    $ python manage.py migrate
    ```
    * now to start the app on localhost:8000 run
    ```
    python manage.py runserver.
    ```
    * now you can access the api by sending a post request to this [endpoint](http://localhost:8000/api/classification)
