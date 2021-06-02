from django_tenants.test.cases import TenantTestCase
from django_tenants.test.client import TenantClient
from django.urls import reverse
from tenants.models import Tenant

class PremiumUserTest(TenantTestCase):
  
  @classmethod
  def setup_tenant(cls, tenant):
    """
    テスト用テナントの設定をここで行う
    """
    tenant.is_premium = True
    return tenant

  def setUp(self) -> None:
    super().setUp()
    self.c = TenantClient(self.tenant)
  
  def tearDown(self) -> None:
    pass

  def test_is_premium(self):
    '''プレミアムユーザーのテナントのトップページを開いたときプレミアムフラグがついている事'''
    response = self.c.get(reverse('diary:index'))
    print(response.status_code)
    self.assertEqual(True, response.context['tenant'].is_premium)
