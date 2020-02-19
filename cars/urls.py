from django.urls import path
from . import views
urlpatterns = [
  path("dashboard", views.index),
  path("newcar", views.newCar),
  path("proc_car", views.proc_car)
]