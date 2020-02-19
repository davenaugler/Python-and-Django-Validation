from django.db import models
from auth_app.models import User
# Create your models here.
class CarManager(models.Manager):
  def validate_new_car(self, requestPOST):
    errors = {}
    print("request post data", requestPOST)
    return errors

class Car(models.Model):
  year = models.IntegerField()
  make = models.CharField(max_length=255)
  model = models.CharField(max_length=255)
  imgUrl = models.URLField()
  user = models.ForeignKey(User, related_name="cars", on_delete=models.CASCADE)
  objects = CarManager()