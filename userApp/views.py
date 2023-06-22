from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from .forms import PostForm
from login_register.models import Users
from .models import Posts, Follow





# Create your views here.

@login_required(login_url='login_register:login')
def home_view(request):
    print(request.user.id)
    return render(request, 'userApp/home.html')


@login_required(login_url='login_register:login')
def profile_view(request):
    user = Users.objects.get(id=request.user.id)
    follower_count = user.followers.all().count()
    following_count = user.following.all().count()
    post_count = Posts.objects.filter(user_id=user).count()
    user_images = Posts.objects.filter(user_id=user)
    profile = {
        'username': user.username,
        'bio': user.bio,
        'followers': following_count,
        'following': follower_count,
        'post_count': post_count,
        'posts': user_images
    }
    print(profile)
    return render(request, 'userApp/profile.html', profile)

@login_required(login_url='login_registerApp:login')
def post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user
            post.save()
            return redirect('home')  # Replace 'home' with the URL name of the desired redirect page
    else:
        form = PostForm()

    return render(request, 'home.html', {'form': form})
    


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user
            post.save()
            return redirect('home')  # Replace 'home' with the URL name of the desired redirect page
    else:
        form = PostForm()

    return render(request, 'post_form.html', {'form': form})



    
