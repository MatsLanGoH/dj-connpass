from django.shortcuts import render

from .tasks import get_events_data_task

# Create your views here.
# connpass = Connpass()
# print(connpass.search(keyword='django'))


def index(request):
    return render(request, 'index.html')


def loading(request):
    return render(request, 'loading.html')


def results(request):
    # return render(request, 'results.html')
    # context = RequestContext(request, processors=[event_proc])
    # context = event_proc(request)
    # context = get_events_data_task.delay()
    context = get_events_data_task()
    # return render(request, 'results.html')
    return render(request, 'results.html', {'events': context})

