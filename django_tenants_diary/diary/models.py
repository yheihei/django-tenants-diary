from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

# Create your models here.
class User(AbstractUser):
  pass


class Post(models.Model):
  user = models.ForeignKey(User, on_delete=CASCADE)
  title = models.CharField(max_length=2048)
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
