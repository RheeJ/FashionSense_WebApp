FROM python:2.7
ENV PYTHONUNBUFFERED 1

WORKDIR /app

#VOLUME ./

RUN apt-get upgrade
RUN apt-get update && apt-get install -y cmake

RUN apt-get update && apt-get install -y dos2unix
RUN pip install Django==1.10.2 \
	djangorestframework==3.4.7 \
	gunicorn==19.6.0

ADD . /app/
ADD start.sh /start.sh
RUN pip install bs4==0.0.1
RUN pip install requests

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8080
RUN dos2unix start.sh
CMD /bin/bash start.sh
