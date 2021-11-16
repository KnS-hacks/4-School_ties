from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import User
from django.contrib import auth

# Create your views here.
def login(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password2"]:
            user = User.objects.create_user(
                username = request.POST["username"],
                password = request.POST["password"],
                email = request.POST["email"],
                uni_num = request.POST["uni_num"],
                status = request.POST["status"],
                card = request.FILES["card"],
            )
            if request.POST["status"] == "학부생":
                user.is_active = False
            else:
                user.is_staff = True 

            user.save()
            # auth.login(request, user)
            # return redirect('home')
            return render(request, 'home.html')    
        else:
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')