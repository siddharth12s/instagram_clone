from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from .forms import PostForm
from login_register.models import Users
from .models import Posts, Follow
from django.http import JsonResponse
import random
from django.views.decorators.csrf import csrf_protect





# Create your views here.
@csrf_protect
@login_required(login_url='login_register:login')
def home_view(request):
    user = request.user
    followed_users = Follow.objects.filter(follower_id=user).values_list('following_id', flat=True)
    posts = list(Posts.objects.filter(user_id__in=followed_users).prefetch_related('user_id').order_by('-created_at'))
    print(posts)
    random.shuffle(posts)
    return render(request, 'userApp/home.html', {'posts': posts})


def search_view(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_query', '')
        users = Users.objects.filter(username__istartswith=search_query)
        userDataList = [user.username for user in users]
        print(userDataList)
        return JsonResponse(userDataList, safe=False)
        # return render(request, 'userApp/home.html', {'userDataList': userDataList})
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
@csrf_protect
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
    

@csrf_protect
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


def other_profile(request, username):
    try:
        user = Users.objects.get(username=username)
        print(user.email_address)
        follower_count = user.followers.all().count()
        following_count = user.following.all().count()
        post_count = Posts.objects.filter(user_id=user).count()
        user_images = Posts.objects.filter(user_id=user)
        is_following = Follow.objects.filter(follower_id=user, following_id=request.user.id).exists()
        profile = {
            'username': user.username,
            'bio': user.bio,
            'followers': following_count,
            'following': follower_count,
            'post_count': post_count,
            'posts': user_images,
            'following_button': is_following
        }
        return render(request, 'userApp/differentProfile.html', profile)
    except Users.DoesNotExist:
        return render(request, 'userApp/differentProfile.html')
    

def follow_unfollow(request, username):
    user_to_follow = Users.objects.get(username=username)
    current_user = request.user
    
    is_following = Follow.objects.filter(following_id=user_to_follow, follower_id=current_user).exists()
    
    if is_following:
        Follow.objects.filter(following_id=user_to_follow, follower_id=current_user).delete()
    else:
        Follow.objects.create(following_id=user_to_follow, follower_id=current_user)
    
    return redirect('other_profile', username=username)