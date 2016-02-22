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
        if not email:
            messages.add_message(request, messages.INFO, 'Please enter an email.')
            return HttpResponseRedirect('/')
        password = request.POST['password']
        if not password:
            messages.add_message(request, messages.INFO, 'Please enter a password.')
            return HttpResponseRedirect('/')
        elif len(password) > 50:
            messages.add_message(request, messages.INFO, 'Password cannot be more than 50 characters')
            return HttpResponseRedirect('/')
        full_name = request.POST['fl_name']
        if not full_name:
            messages.add_message(request, messages.INFO, 'Please enter a name.')
            return HttpResponseRedirect('/')
        elif len(full_name) > 50:
            messages.add_message(request, messages.INFO, 'Name cannot be more than 50 characters')
            return HttpResponseRedirect('/')
            
        if User.objects.filter(username=email).exists():
            messages.add_message(request, messages.INFO, 'Account with this email already exists!')
            return HttpResponseRedirect('/')
        else: 
            user = User.objects.create_user(email, email, password)
            user.first_name = full_name.split()[0]
            user.save()
            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/')

        
    return HttpResponseRedirect('/')
