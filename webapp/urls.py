from django.conf.urls import url, include
import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'classification', views.ClassificationView, base_name='classification')
# router.register(r'test', TestViewSet)

urlpatterns = [
    url(r'classification', views.ClassificationView.as_view()),
	url(r'^', include(router.urls)),
	# url(r'^view', test_view),
]
