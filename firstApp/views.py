from django.shortcuts import render, redirect
import random

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from . import circuit_functions


display_matrix = [[1, 0],
                  [0, 1]]

# Create your views here.
def home(request):
   context = {"name": request.user}
   return render(request, "firstApp/home.html", context)

def tool(request):
   context = {"name": request.user,
              "matrix": display_matrix}
   return render(request, "firstApp/tool.html", context)

def login_view(request):
  context = {
    "login_view": "active"
  }
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect("home")
    else:
      return HttpResponse("Sorry, you fool, that's wrong")
  return render(request, "registration/login.html", context)

def logout_view(request):
    logout(request)
    return redirect("home")

def add_rail(request):
    context = {
        "matrix": circuit_functions.add_qubit(display_matrix)
    }
    return render(request, "firstApp/tool.html", context)

def qiskit_view(request):
    pass


class SignUp(CreateView):
    """Class for user creation"""
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
