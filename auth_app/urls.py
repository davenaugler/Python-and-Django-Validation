from django.urls import path
from . import views
urlpatterns = [
  path("", views.index),
  path("login", views.login),
  path("register", views.register),
  path("proc_reg", views.proc_reg),
  path("proc_login", views.proc_login),
]