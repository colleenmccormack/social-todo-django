from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .forms import TaskForm
from .forms import NameForm

# Create your views here.

# def index(request):
#     template = loader.get_template('index.html')
#     return HttpResponse("Hello, world. You're at the tasks index. There's still much go do.")
    
def say_whatsup(request):
    return HttpResponse("Hello, WHAT IS UP?")

def get_task(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TaskForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TaskForm()

    return render(request, 'tasks.html', {'form': form})

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})