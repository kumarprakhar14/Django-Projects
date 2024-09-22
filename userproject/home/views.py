from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout

# Users:
# 1. admin(password: admin)
# 2. user(password: user@8987)

# Create your views here.
def index(request):
   # check if user is logged in
   if request.user.is_anonymous:
       return redirect("/login")
   return render(request, 'index.html')

def loginUser(request):
   if request.method == 'POST':
   # check if user has entered correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
   else: 
        return render(request, 'login.html', {'error': 'Invalid username or password'})

def logoutUser(request):
   logout(request)
   return redirect("/login")