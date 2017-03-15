from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('app/index.html')
    #context = RequestContext(request, {})
    return HttpResponse(template.render())