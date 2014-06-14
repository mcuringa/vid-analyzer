import random
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib import messages

from vidan.models import *

def home(request):
    
    context = {"foo": "this is a test"}

    return render(request, 'home.html', context)



