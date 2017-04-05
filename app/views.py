from django.http import HttpResponse
from django.template import loader

def index(request):
    template = None
    if request.method == 'GET':
        template = loader.get_template('app/index.html')
        return HttpResponse(template.render())
    elif request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print form
        if form.is_valid():
            print form
            return HttpResponseRedirect('/success/url/')
