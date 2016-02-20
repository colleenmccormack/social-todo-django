from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from .models import Task

# Create your views here.

def tasks(request):
    task_list = Task.objects.all()
    return render(request, 'index.html', { 'task_list': task_list })

def create(request):
	if request.method == 'POST':
		title = request.POST['title']
		description = request.POST['description']
		current_user = request.user
		if current_user.is_authenticated():
			print current_user.id
		# user = User.objects.create_user("joe@yale.edu", "joe@yale.edu", "blah")
		# user = authenticate(username="joe@yale.edu", password="blah")
		task = Task.objects.create_task(current_user, title, description)
	# return HttpResponseRedirect('https://www.facebook.com/')
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
