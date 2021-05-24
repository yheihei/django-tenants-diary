from django.db import models
from django.db.models.deletion import CASCADE
from user.models import User

# Create your models here.
class Post(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey(User, on_delete=CASCADE)
  title = models.CharField(max_length=2048)
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
