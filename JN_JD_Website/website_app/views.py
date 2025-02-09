import time
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignInForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
@login_required
def home(request):
    # You can populate the context with data specific to the user or the page
    context = {}
    return render(request, 'home.html', context)

def about(request):
    # About page context, you can update it if necessary
    context = {}
    return render(request, 'index.html', context)

def create_account(request):
    # This is the login page view
    context = {}
    return render(request, 'createaccount.html', context)

def sign_in(request):
    if request.method == "POST":
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)

            # Handle the remember me functionality
            if not form.cleaned_data.get('remember_me'):
                request.session.set_expiry(0)
            return redirect('home')
    else:
        form = SignInForm()

    # Context for the signin page to display the form
    context = {
        'form': form
    }
    return render(request, 'signin.html', context)

def edit_groups(request):
    # This is the login page view

    ## CONNECT TO PAGE AND SYNC WITH DB
    context = {

    }
    return render(request, 'editgroups.html', context)

def edit_event(request):
    # This is the login page view

    ## CONNECT TO PAGE AND SYNC WITH DB
    timestamp = str(int(time.time()))
    context = {
        'timestamp': timestamp,
    }
    return render(request, 'editevent.html', context)


def view_events(request):
    # This is the login page view

    context = {
    }
    return render(request, 'viewevents.html', context)


