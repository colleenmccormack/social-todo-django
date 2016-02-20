from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render_to_response  

from .models import Task

# Create your views here.

def index(request):
    task_list = Task.objects.all()
    return render(request, 'index.html', { 'task_list': task_list })
