from django_tenants.test.cases import TenantTestCase
from django_tenants.test.client import TenantClient
from django.urls import reverse
from tenants.models import Tenant
from user.models import User
from diary.models import Post
from django.core.management import call_command


class IndexPageTest(TenantTestCase):
  @staticmethod
  def get_test_schema_name():
    '''テスト用テナントのschema名を定義'''
    return 'test'

  @classmethod
  def setup_tenant(cls, tenant):
    """
    テスト用テナントの設定
    """
    tenant.is_premium = True # プレミアムユーザー
    return tenant

  def setUp(self) -> None:
    super(IndexPageTest, self).setUp()
    # テスト用テナントでアクセスするためのクライアント
    self.c = TenantClient(self.tenant)
    
    # 日記コンテンツを投入する(schema指定しなくてもテスト用テナントに入る)
    call_command('loaddata', 'diary/fixtures/tests/user.json')
    call_command('loaddata', 'diary/fixtures/tests/diary.json')
  
  def tearDown(self) -> None:
    pass

  def test_is_premium(self):
    '''プレミアムユーザーのテナントのトップページを開いたときプレミアムフラグがついている事'''
    response = self.c.get(reverse('diary:index'))
    self.assertEqual(True, response.context['tenant'].is_premium)
  
  def test_is_post(self):
    '''トップページを開いた際日記コンテンツが表示されていること'''
    response = self.c.get(reverse('diary:index'))
    self.assertEqual('日記1', response.context['posts'][0].title)
    self.assertEqual('<p>日記だよ', response.context['posts'][0].body)
