import os,binascii
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

        file_obj = request.data['file']

        print "saving image"
        filename = binascii.b2a_hex(os.urandom(15)) + '.jpg'
        with open("/tmp/" + filename, 'wb+') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)

        filepath = { "file_path" : "/tmp/" + filename }
        endpoint = "http://ml:5000"
        headers = {"Content-Type":"application/json"}
        r = requests.post(endpoint, json=filepath, headers=headers)
        classification = r.json()

        os.remove("/tmp/" + filename)

        return Response(classification)
