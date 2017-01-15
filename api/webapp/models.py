from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class test_model(models.Model):
	attribute = models.CharField(max_length=50)

