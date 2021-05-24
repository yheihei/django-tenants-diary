from django.contrib import admin

# Register your models here.
from tenants.models import Tenant, Domain

admin.site.register(Tenant, admin.ModelAdmin) # テナント登録をテナント側から非表示にしたければここに含めない
admin.site.register(Domain, admin.ModelAdmin) # ドメイン登録をテナント側から非表示にしたければここに含めない