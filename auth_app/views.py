from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
  return redirect("/login")

def login(request):
  return render(request, "login.html")

def register(request):
  return render(request, "register.html")

def proc_reg(request):
  if request.method != "POST":
    return redirect("/auth/login")
  errors = User.objects.validate_reg(request.POST)
  if len(errors):
    for key, anError in errors:
      messages.error(request, errors[key])
    return redirect("/auth/register")
  hashed = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()).decode()
  newUser = User.objects.create(fName=request.POST["fName"],lName=request.POST["lName"],email=request.POST["email"], password=hashed)
  request.session['userId'] = newUser.id
  return redirect("/dashboard")

def proc_login(request):
  user = User.objects.filter(email=request.POST["email"])
  if not user:
    messages.error(request, "Email does not exist")
    return redirect("/auth/login")
  if bcrypt.checkpw(request.POST["password"].encode(), user[0].password.encode()):
    request.session["userId"] = user[0].id
    return redirect("/dashboard")

