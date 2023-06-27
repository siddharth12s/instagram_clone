from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from .forms import PostForm, EditForm
from login_register.models import Users
from login_register.views import login_view
from .models import Posts, Follow
from django.http import JsonResponse
import random
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout





# Create your views here.
@csrf_protect
@login_required(login_url=login_view)
def home_view(request):
    user = request.user
    followed_users = Follow.objects.filter(follower_id=user).values_list('following_id', flat=True)
    posts = list(Posts.objects.filter(user_id__in=followed_users).prefetch_related('user_id').order_by('-created_at'))
    user_posts = list(Posts.objects.filter(user_id=request.user))
    all_posts = posts + user_posts
    print(posts)
    random.shuffle(all_posts)
    return render(request, 'userApp/home.html', {'posts': all_posts, 'profile_img': user.profile_image})

@login_required(login_url=login_view)
def search_view(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_query', '')
        users = Users.objects.filter(username__istartswith=search_query)
        userDataList = [user.username for user in users]
        return JsonResponse(userDataList, safe=False)
        # return render(request, 'userApp/home.html', {'userDataList': userDataList})
    return render(request, 'userApp/home.html')


@login_required(login_url=login_view)
def profile_view(request):
    user = Users.objects.get(id=request.user.id)
    follower_count = user.followers.all().count()
    following_count = user.following.all().count()
    post_count = Posts.objects.filter(user_id=user).count()
    user_images = Posts.objects.filter(user_id=user)
    profile = {
        'username': user.username,
        'bio': user.bio,
        'profile_pic': user.profile_image,
        'followers': following_count,
        'following': follower_count,
        'post_count': post_count,
        'posts': user_images
    }
    # print(profile)
    return render(request, 'userApp/profile.html', profile)

@login_required(login_url=login_view)
@csrf_protect
def post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user
            post.save()
            return redirect('home') 
    else:
        form = PostForm()

    return render(request, 'home.html', {'form': form})
    

@csrf_protect
@login_required(login_url=login_view)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user
            post.save()
            return redirect('home')  
    else:
        form = PostForm()

    return render(request, 'post_form.html', {'form': form})

@login_required(login_url=login_view)
def other_profile(request, username):
    try:
        user = Users.objects.get(username=username)
        follower_count = user.followers.all().count()
        following_count = user.following.all().count()
        post_count = Posts.objects.filter(user_id=user).count()
        user_images = Posts.objects.filter(user_id=user)
        sidebar_profile_img = request.user.profile_image
        is_following = Follow.objects.filter(follower_id=user, following_id=request.user.id).exists()
        profile = {
            'username': user.username,
            'profile_pic': user.profile_image,
            'bio': user.bio,
            'followers': following_count,
            'following': follower_count,
            'post_count': post_count,
            'posts': user_images,
            'following_button': is_following,
            'sidebar_profile_img': sidebar_profile_img,
        }
        return render(request, 'userApp/differentProfile.html', profile)
    except Users.DoesNotExist:
        return render(request, 'userApp/differentProfile.html')
    
@login_required(login_url=login_view)
def follow_unfollow(request, username):
    user_to_follow = Users.objects.get(username=username)
    current_user = request.user
    
    is_following = Follow.objects.filter(following_id=user_to_follow, follower_id=current_user).exists()
    
    if is_following:
        Follow.objects.filter(following_id=user_to_follow, follower_id=current_user).delete()
    else:
        Follow.objects.create(following_id=user_to_follow, follower_id=current_user)
    
    return redirect('other_profile', username=username)

@csrf_protect
@login_required(login_url=login_view)
def edit_profile(request, username):
    updating_user = get_object_or_404(Users, username=username)
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=updating_user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    
    return redirect('profile')

@login_required(login_url=login_view)
def logout_view(request):
    logout(request)
    return redirect('login') 