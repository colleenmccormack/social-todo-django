from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import get_messages, add_message

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/task/')
    else:
        storage = get_messages(request)
        error = None
        for message in storage:
            error = message
            break
        return render(request, 'index.html', {'errors': error})

def todo_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
        	if user.is_active:
        		login(request, user)
        		return HttpResponseRedirect('/')
        else:
            if User.objects.filter(username=email).exists():
                messages.add_message(request, messages.INFO, 'Invalid password')
            else:
                messages.add_message(request, messages.INFO, 'Invalid email address')
            return HttpResponseRedirect('/')

        return HttpResponseRedirect('/')

def todo_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        full_name = request.POST['fl_name']
        split_name = full_name.split()
        if User.objects.filter(username=email).exists():
            messages.add_message(request, messages.INFO, 'Account with this email already exists!')
            return HttpResponseRedirect('/')
        else: 
            user = User.objects.create_user(email, email, password)
            user.first_name = split_name[0]
            user.save()
            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/')
            
        
    return HttpResponseRedirect('/')
