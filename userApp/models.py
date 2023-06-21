from django.db import models
from login_register.models import Users

# Create your models here.
class Posts(models.Model):
    post_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    caption = models.CharField(max_length=50, blank=True)
    is_image = models.BooleanField(default=True)
    image = models.ImageField(upload_to='post_images', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Follow(models.Model):
    follow_id = models.AutoField(primary_key=True)
    following_id = models.ForeignKey(Users, related_name='followers', on_delete=models.CASCADE)
    follower_id = models.ForeignKey(Users, related_name='following', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)