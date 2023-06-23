from django.contrib import admin

# Register your models here.
from django.db import models
from .models import Follow, Posts

admin.register(Follow)
admin.register(Posts)