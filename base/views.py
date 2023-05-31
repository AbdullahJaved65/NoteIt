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
def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user_db = User.objects.get(username='username')
        except User.DoesNotExist:
            messages.error(request, 'The User does not exist!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR Password is invalid')

    context = {'page': page}
    return render(request, 'base/login.html', context)


def logoutUser(request):
    logout(request)
    redirect('home')


def registerUser(request):
    page = 'register'
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            redirect('home')
        else:
            messages.error(request, 'Something went wrong')

    context = {'page': page, 'form': form}
    return render(request, 'base/register.html', context)


def home(request):
    context = {}
    return render(request, 'base/home.html', context)
