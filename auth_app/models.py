from django.db import models

# Create your models here.
class UserManager(models.Manager):
  def validate_reg(self, registrationData):
    errors = {}
    print("Printing the registration data")
    return errors


class User(models.Model):
  fName=models.CharField(max_length=255)
  lName=models.CharField(max_length=255)
  email=models.CharField(max_length=255)
  password=models.CharField(max_length=255)
  objects=UserManager()

