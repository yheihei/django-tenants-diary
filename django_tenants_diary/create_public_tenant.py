import os
import sys


# sys.path.append(os.path.dirname(__file__))
def main(domain_name):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_tenants_diary.settings')
    import django
    from django.core.management.commands.runserver import Command as runserver
    from django.core.management import execute_from_command_line
    django.setup()
    from tenants.models import Tenant, Domain

    Tenant.objects.all()
    tenant = Tenant(schema_name='public', name='admin tenant')
    tenant.save()

    domain = Domain()
    domain.domain = domain_name
    domain.tenant = tenant

    domain.is_primary = True
    domain.save()


if __name__ == '__main__':
    domain = input('domain: ')
    main(domain)
