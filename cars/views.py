from django.shortcuts import render, redirect
from .models import Car
from auth_app.models import User
# Create your views here.
def index(request):
  if not "userId" in request.session:
    return redirect("/auth/login")
  
  return render(request, "index.html",{
    "cars": Car.objects.all()
  })

def newCar(request):
  return render(request, "newcar.html")

def proc_car(request):
  if request.method == "POST":
    year = request.POST["year"]
    make = request.POST["make"]
    model = request.POST["model"]
    imgUrl = request.POST["imgUrl"]
    user = User.objects.get(id=request.session["userId"])
    Car.objects.create(
      year=year,
      make=make,
      model=model,
      imgUrl=imgUrl,
      user=user
    )
    return redirect("/dashboard")
  return redirect("/newcar")