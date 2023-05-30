from django.shortcuts import render
from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.db.models import Q
from django.db.models import QuerySet

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    context = {}
    return render(request, 'base/home.html', context)
