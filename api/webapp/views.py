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


class ClassificationView(APIView):
    """
    given a request with image data,
    returns a json response of the classification
    """

    renderer_classes = (JSONRenderer, )
    parser_classes = (FileUploadParser,)

    def post(self, request, format=None):

        meta = request.META
        if 'Content-Type' not in meta:
            raise SuspiciousOperation("Invalid request; see documentation for correct paramaters")

        content_type = meta['Content-Type'].split('/')
        if content_type[0] != 'image':
            raise SuspiciousOperation("Invalid request; see documentation for correct paramaters")

        file_obj = request.data['file']
        # with open('pic.jpg', 'wb+') as f:
        #     for chunk in file_obj.chunks():
        #         f.write(chunk)

        classification = {"classification":"formal"}
        return Response(classification)
