from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib import messages


from vidan.models import *

def home(request):

    return render(request, 'home.html')

def login_user(request):


    action = request.POST['login']
    username = request.POST['username']
    password = request.POST['password']

    if action == "join":
        if len(username) == 0:
            messages.add_message(request, messages.INFO, 'You must provide a username.')
            return HttpResponseRedirect('/')
        if len(password) < 3:
            messages.add_message(request, messages.INFO, 'You must provide a password of at least 3 chars.')
            return HttpResponseRedirect('/')

        user = User.objects.create_user(username=username, password=password)
        messages.add_message(request, messages.INFO, 'Welcome to the video analyzer.')

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        messages.add_message(request, messages.INFO, 'You are successfully logged in, ' + username)
        return HttpResponseRedirect('/dataset')
    
    messages.add_message(request, messages.INFO, 'Sorry, we could not log you in with that username and password.')
    return HttpResponseRedirect('/home')

@login_required
def dataset(request):
    form = DataSetForm()
    context = { "form": form }
    return render(request, 'dataset.html', context)

@login_required
def upload(request):

	return render(request, 'upload.html')


