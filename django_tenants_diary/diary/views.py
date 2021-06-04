from django.shortcuts import render
from .models import Post
from function_setting.models import Category as CategoryFunction

# Create your views here.
def index(request):

  is_category_function = False
  try:
    is_category_function = CategoryFunction.objects.get(tenant=request.tenant).is_enable
    print(is_category_function)
  except CategoryFunction.DoesNotExist:
    pass

  return render(request, 'index.html', {
    'posts': Post.objects.all(),
    'tenant': request.tenant,
    'is_category_function': is_category_function,
  })
