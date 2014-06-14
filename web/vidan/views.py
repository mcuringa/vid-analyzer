import random
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib import messages

from vidan.models import *

def home(request):
    term = request.POST["query"]
    vidList = videos.search(term)
    
    context = {"videos": vidList}

    return render(request, 'home.html', context)

def upload(request):


	return render(request, 'upload.html')


