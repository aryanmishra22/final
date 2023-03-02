from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout

# Create your views here.
def home(request):
    user = request.user
    return render(request, 'final_web/index.html', {})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'final_web/signup.html', {'form': form})

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            dj_login(request, user)
            fname = user.first_name
            return render(request, 'final_web/index.html', {'fname': fname})
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
        
    return render(request, 'final_web/login.html', {})

def logout(request):
    dj_logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('home')