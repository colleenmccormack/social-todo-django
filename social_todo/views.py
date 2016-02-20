from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')

def todo_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
        	if user.is_active:
        		login(request, user)
        		return render(request, 'index.html')
        else:
        	return render(request, 'index.html', {'errors': "Username/Password Incorrect"})

        return render(request, 'index.html')

def logout(request):
    pass

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
        		return render(request, 'index.html')
        else:
        	return render(request, 'index.html', {'errors': "Username/Password Incorrect"})
        print user
    return render(request, 'index.html')
