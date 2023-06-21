from django.urls import path
from userApp.views import profile_view, post_view,home_view

urlpatterns = [
    path('home/', home_view, name='home'),
    path('profile/', profile_view, name='profile'),
    path('profile/post/', post_view, name='posts')
]
