from django.contrib import admin
from .models import User, Post, Category

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Category)
