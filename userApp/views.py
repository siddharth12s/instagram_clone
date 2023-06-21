from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from .forms import PostForm


# Create your views here.

@login_required(login_url='login_register:login')
def home_view(request):
    print(request.user.id)
    return render(request, 'userApp/home.html')


@login_required(login_url='login_register:login')
def profile_view(request):
    print(request.user)
    return render(request, 'userApp/profile.html')

@login_required(login_url='login_registerApp:login')
def post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user.id
            post.save()
            return redirect('home')
    return render(request, 'userApp/posts.html')