FROM python:2.7
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get upgrade
RUN apt-get update && apt-get install -y cmake

#---------------------------OPENCV BUILD--------------------------------
RUN apt-get install -y wget

RUN apt-get install -y build-essential cmake git pkg-config \
	libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev \
    libgtk2.0-dev \
    libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
    libatlas-base-dev gfortran

RUN apt-get install -y unzip
RUN pip install numpy

RUN wget https://github.com/Itseez/opencv/archive/3.0.0.zip && \
	unzip 3.0.0.zip && \
	rm 3.0.0.zip
RUN wget https://github.com/Itseez/opencv_contrib/archive/3.0.0.zip && \
	unzip 3.0.0.zip && \
	rm 3.0.0.zip

RUN mkdir ./opencv-3.0.0/build
WORKDIR ./opencv-3.0.0/build
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE \
	 -D BUILD_opencv_python=ON \
 	 -D CMAKE_INSTALL_PREFIX=/usr/local \
	 -D INSTALL_C_EXAMPLES=ON \
	 -D INSTALL_PYTHON_EXAMPLES=ON \
 	 -D OPENCV_EXTRA_MODULES_PATH=/opencv_contrib-3.0.0/modules \
 	 -D BUILD_EXAMPLES=ON \
	 -D BUILD_NEW_PYTHON_SUPPORT=ON \
	 -D WITH_IPP=OFF \
 	 -D WITH_V4L=ON ..
RUN make -j4

RUN make install
RUN ldconfig

WORKDIR /app
RUN cp opencv-3.0.0/build/lib/cv2.so /usr/local/lib/python2.7/dist-packages
RUN ls /usr/local/lib/python2.7/site-packages
RUN echo "import cv2 \nprint(cv2.__version__)" >> test.py
RUN python test.py

#------------------------DJANGO APPLICATION BUILD-------------------------
RUN apt-get update && apt-get install -y dos2unix 
RUN pip install Django==1.10.2 \
	djangorestframework==3.4.7 \
	gunicorn==19.6.0

ADD . /app/
ADD start.sh /start.sh
RUN pip install bs4==0.0.1

#------------------------EXPOSE AND SET UP CONTAINER TO RUN-----------------
EXPOSE 8080
RUN dos2unix start.sh
CMD /bin/bash start.sh