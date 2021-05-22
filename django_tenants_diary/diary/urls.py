from django.urls import path
from . import views

app_name = "auctions"
urlpatterns = [
  path("", views.index, name="index"),
]
