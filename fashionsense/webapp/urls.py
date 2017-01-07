from django.conf.urls import url, include
from views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'test', TestViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^view', test_view),
]