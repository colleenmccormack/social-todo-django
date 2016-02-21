from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Task
from itertools import chain

def tasks(request):
    current_username = request.user.username
    owned = Task.objects.filter(owner = request.user)
    collaborating = Task.objects.filter(collaborators__username = current_username)
    task_list = list(chain(owned, collaborating))
    for task in task_list:
    	if task.owner == request.user:
    		task.isOwnedByCurrentUser = True
    	else:
			task.isOwnedByCurrentUser = False
    return render(request, 'index.html', { 'task_list': task_list })

def delete(request, task_id="1"):
	current_task = Task.objects.get(id = task_id)
	current_task.delete()
	return render(request, 'index.html', { 'isOwner': isOwner })
	# return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def complete(request, task_id="1"):
	current_task = Task.objects.get(id = task_id)
	if current_task.completed:
		current_task.completed = False
	else:
		current_task.completed = True
	current_task.save()
	print current_task.completed
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

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
				return render(request, 'index.html', {'errors': "You added a collaborator (" + c2 + ") that does not exist"})
		if c3:
			if User.objects.filter(username=c3).exists():
				task.collaborators.add(User.objects.get(username = c3))
			else:
				return render(request, 'index.html', {'errors': "You added a collaborator (" + c3 + ") that does not exist"})

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
