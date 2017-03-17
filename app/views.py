from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('app/index.html')
    # host, port = request.get_host().split(':')
    return HttpResponse(template.render())
