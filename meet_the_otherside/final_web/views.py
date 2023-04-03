from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from .forms import RegisterForm, PostForm
from .models import Profile, Post

# Create your views here.
def home(request):
    user = request.user
    form = PostForm()
    return render(request, 'final_web/index.html', {'form':form})

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
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
        
    return render(request, 'final_web/login.html', {})

def logout(request):
    dj_logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('home')

def post(request):
    user = request.user
    if user.is_authenticated:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            if request.method == 'POST':
                post = Post()
                post.user = user
                post.title = request.POST['title']
                post.body = request.POST['body']
                post.reliability = 50
                post.save()
                # for image in request.FILES.getlist('images'):
                #     ("reached image loop")
                #     post_image = PostImages()
                #     post_image.post = post
                #     post_image.image = image
                #     post_image.save()
                return redirect('home')
        else:
            context = {'form': form}
            return render(request, 'final_web/index.html', context)
    redirect('home')

def profile(request, username):
    form = PostForm()
    user = request.user
    if user.is_authenticated:
        profile_user = User.objects.get(username=username)
        profile_data = Profile.objects.get(user=profile_user)
        fname = user.first_name
        posts = Post.objects.filter(user=profile_user)
        context = {'fname': fname,'profile_data': profile_data, 'username': user.username, 'form': form , 'posts': posts}
        return render(request, 'final_web/profile.html', context)
    return render(request, 'final_web/login.html', {})

def search(request):
    form = PostForm()
    return render(request, 'final_web/search.html', {'form':form})