from webapp.models import *
from rest_framework import serializers

class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = test_model
        fields = (['attribute'])