from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Tenant(TenantMixin):
    name = models.CharField(max_length=100)
    is_premium = models.BooleanField(default=False, verbose_name="プレミアムユーザーかどうか")
    def __str__(self):
        return self.name


class Domain(DomainMixin):
    pass
