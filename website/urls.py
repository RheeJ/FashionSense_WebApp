from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('app.urls')),
    url(r'^quiz/', include('quiz.urls')),
]
