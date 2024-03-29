from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages

from application.models import Category, Application
from .forms import SignupForm

def index(request):
    applications = Application.objects.filter(appstate=3)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'applications': applications,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged out...")
    return render(request, 'core/index.html')