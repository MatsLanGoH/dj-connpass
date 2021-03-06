from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import get_template

from .forms import QueryForm
from .tasks import get_events_data_task


# Create your views here.
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QueryForm(request.POST)
        # check whether it's valid
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            return render(request, 'results.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QueryForm()

    return render(request, 'index.html', {'form': form})


def loading(request):
    if request.method == 'GET':
        return redirect('index')

    return render(request, 'loading.html')


def results(request):
    if request.method == 'POST':
        if request.is_ajax():
            import json
            t = get_template('results.html')
            json_str = request.body.decode(encoding='UTF-8')
            json_obj = json.loads(json_str)
            context = get_events_data_task(json_obj)
            html = t.render({'events': context})
            return HttpResponse(html)

    return redirect('index')



