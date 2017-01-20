from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework import viewsets
from webapp.models import  *
from webapp.serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from django.core.files.storage import default_storage
from django.core.exceptions import SuspiciousOperation
import requests
import json


class ClassificationView(APIView):
    """
    given a request with image data,
    returns a json response of the classification
    """

    renderer_classes = (JSONRenderer, )
    parser_classes = (FileUploadParser,)

    def post(self, request, format=None):

        try:
            file_obj = request.data['file']
            # with open('pic.jpg', 'wb+') as f:
            #     for chunk in file_obj.chunks():
            #         f.write(chunk)
        except:
            # TODO: implement specific exception handling and logging
            print "Could not find image file"
            raise SuspiciousOperation("Invalid request")


        try:
            features = { "features" : [0, 1, 0, 1, 6] }
            #host = "https://jsonplaceholder.typicode.com/"
            endpoint = "http://ml:5000"# host + "posts"
            r = requests.post(endpoint, data=features)
            classification = r.json()
        except:
            print "Could not get ml"
            raise SuspiciousOperation("Invalid request")

        return Response(classification)
