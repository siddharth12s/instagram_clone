from django.urls import path
from userApp.views import profile_view, post_view,home_view,create_post,search_view, other_profile, follow_unfollow, edit_profile

urlpatterns = [
    path('home/', home_view, name='home'),
    path('profile/', profile_view, name='profile'),
    path('post/', post_view, name='posts'),
    path('create/', create_post, name='create_post'),
    path('search/', search_view, name='search'),
    path('profile/<str:username>/', other_profile, name='other_profile'),
    path('follow-unfollow/<str:username>/', follow_unfollow, name='follow_unfollow'),
    path('edit-profile/<str:username>/', edit_profile, name='edit')
]
