from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request):
	if request.user.is_authenticated():
		url = HttpResponseRedirect('http://127.0.0.1:8000/task/')
	else:
		url = render(request, 'index.html')
	return url

def todo_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
        	if user.is_active:
        		login(request, user)
        		# return render(request, 'index.html')
        		return HttpResponseRedirect(request.META.get('HTTP_REFERER')+'task/')
        else:
		    # figure out how to make this the home url
		    return render(request, 'index.html', {'errors': "Username/Password Incorrect"})

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def todo_logout(request):
    logout(request)
    # gotta be a better way to do this
    return HttpResponseRedirect('http://127.0.0.1:8000/')

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(email, email, password)
        user.first_name = request.POST['fl_name']
        user.save()
        user = authenticate(username=email, password=password)
        if user is not None:
        	if user.is_active:
        		login(request, user)
        		return HttpResponseRedirect(request.META.get('HTTP_REFERER')+'task/')
        else:
        	return render(request, 'index.html', {'errors': "Username/Password Incorrect"})
        print user
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
