from django.shortcuts import render, redirect, get_object_or_404
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
        if user is not None: # user가 있고
            if user.approval == "승인완료": # approval이 승인완료이면
                django_login(request, user) # 로그인
                return redirect('home')
            elif user.approval == "승인대기": # approval이 승인대기이면
                return render(request, 'login.html', {'error':'승인 대기 중입니다.'}) # 로그인을 막고 승인 대기 문구 출력
        else:
            return render(request, 'login.html', {'error':'아이디와 비밀번호가 일치하지 않습니다.'}) # 아예 user에 없다면 에러문구 출력
    else:
        return render(request, 'login.html')

# 로그아웃
def logout(request):
    django_logout(request)
    return redirect('home')

# 회원가입
def signup(request):
    if request.method == "POST":
        if User.objects.filter(username=request.POST['username']).exists(): #아이디 중복 체크 
            return render(request, 'signup.html', {'error':'사용할 수 없는 아이디 입니다.'})
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
            if request.POST["status"] == "관리자":
                user.approval = "승인완료"
            else:
                user.approval = "승인대기"

            user.save()
            # auth.login(request, user)
            return redirect('home')
            # return render(request, 'home.html')    
        else:
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')