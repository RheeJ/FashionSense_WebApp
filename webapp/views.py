from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework import viewsets
from webapp.models import  *
from webapp.serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

# class TestViewSet(viewsets.ModelViewSet):
# 	queryset = test_model.objects.all()
# 	serializer_class = TestSerializer

class ClassificationView(APIView):
    """
    given a request with image data,
    returns a json response of the classification
    """

    renderer_classes = (JSONRenderer, )

    def post(self, request, format=None):
        classification = {'classification':'formal'}
        return Response(classification)
