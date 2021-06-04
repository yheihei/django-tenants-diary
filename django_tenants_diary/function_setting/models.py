from django.db import models
from django.db.models.deletion import CASCADE
from tenants.models import Tenant

# Create your models here.
class Category(models.Model):
  tenant = models.ForeignKey(Tenant, on_delete=CASCADE)
  is_enable = models.BooleanField(default=True)
