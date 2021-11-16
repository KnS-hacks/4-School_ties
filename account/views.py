from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from .models import User
from django.contrib import auth

# Create your views here.
# 로그인
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        if user is not None:
            django_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error':'아이디와 비밀번호가 맞지 않습니다.'})
    else:
        return render(request, 'login.html')

# 로그아웃
def logout(request):
    django_logout(request)
    return redirect('home')

# 로그아웃
def logout(request):
    django_logout(request)
    return redirect('home')

# 회원가입
def signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password2"]:
            user = User.objects.create_user(
                username = request.POST["username"],
                real_name = request.POST["real_name"],
                password = request.POST["password"],
                email = request.POST["email"],
                uni_num = request.POST["uni_num"],
                status = request.POST["status"],
                card = request.FILES["card"],
            )
            # if request.POST["status"] == "학부생":
            #     user.is_active = False
            # else:
            #     user.is_staff = True 

            user.save()
            # auth.login(request, user)
            return redirect('home')
            # return render(request, 'home.html')    
        else:
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')