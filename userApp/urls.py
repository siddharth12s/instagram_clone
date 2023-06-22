from django.urls import path
from userApp.views import profile_view, post_view,home_view,create_post

urlpatterns = [
    path('home/', home_view, name='home'),
    path('profile/', profile_view, name='profile'),
    path('post/', post_view, name='posts'),
    path('create/', create_post, name='create_post'),
]
