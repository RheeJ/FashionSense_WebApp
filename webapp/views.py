from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework import viewsets
from webapp.models import  *
from webapp.serializers import *

class TestViewSet(viewsets.ModelViewSet):
	queryset = test_model.objects.all()
	serializer_class = TestSerializer

@api_view(['GET'])
def test_view(request):
	return HttpResponse("HelloWorld!")
