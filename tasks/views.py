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
    task_list = Task.objects.filter(owner = request.user).filter(collaborators__id = request.user)
    return render(request, 'index.html', { 'task_list': task_list })

def create(request):
	if request.method == 'POST':
		title = request.POST['title']
		description = request.POST['description']
		
		current_user = request.user
		if current_user.is_authenticated():
			print current_user.id
		else:
			# go back to log in page
			return HttpResponseRedirect('http://127.0.0.1:8000/')

		task = Task.objects.create_task(current_user, title, description)

		c1 = request.POST['collaborator1']
		c2 = request.POST['collaborator2']
		c3 = request.POST['collaborator3']

		if c1:
			if User.objects.filter(username=c1).exists():
				task.collaborators.add(User.objects.get(username = c1))
			else:
				return render(request, 'index.html', {'errors': "You added a collaborator (" + c1 + ") that does not exist"})
		if c2:
			if User.objects.filter(username=c2).exists():
				task.collaborators.add(User.objects.get(username = c2))
			else:
				return render(request, 'index.html', {'errors': "You added a collaborator (" + c1 + ") that does not exist"})
		if c3:
			if User.objects.filter(username=c3).exists():
				task.collaborators.add(User.objects.get(username = c3))
			else:
				return render(request, 'index.html', {'errors': "You added a collaborator (" + c1 + ") that does not exist"})

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
