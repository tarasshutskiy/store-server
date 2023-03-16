from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth
from django.urls import reverse


# Create your views here.
def login(request):
    context = {'form': UserLoginForm()}
    return render(request, 'users/login.html', context)


def register(request):
    context = {'form': UserRegistrationForm()}
    return render(request, 'users/register.html', context)


def profile(request):
    context = {'form': UserProfileForm()}
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
