from django.shortcuts import redirect, render
from .models import *
from django.utils import timezone
# Create your views here.
def home(request):
    return render(request, 'home.html')

### 공지사항
def notice(request):
    Notices = Notice.objects.all()
    return render(request, 'notice.html',{'Notices':Notices})

# 공지사항 create
def notice_post(request):
    if request.method == 'POST':
        new_notice = Notice()
        new_notice.Notice_title = request.POST['title']
        new_notice.Notice_author = request.POST['author']
        new_notice.Notice_image = request.FILES.get('image')
        new_notice.Notice_body = request.POST['body']
        new_notice.Notice_pub_date = timezone.now()
        new_notice.save()
        return redirect('home')
    else:
        return render(request, 'notice_new.html')




###자유게시판
def free_board(request):
    Free_boards = Free_board.objects.all()
    return render(request, 'free.html',{'Free_boards':Free_boards})



### 스터디 게시판 ??
def study_board(request):
    Study_boards = Study_board.objects.all()
    return render(request, 'study.html',{'Study_boards':Study_boards})

### 공모전 게시판
def contest_board(request):
    Contest_boards = Contest_board.objects.all()
    return render(request, 'contest.html',{'Contest_boards':Contest_boards})

### 졸업생 게시판
def graduate_board(request):
    Graduate_boards = Graduate_board.objects.all()
    return render(request, 'graduate.html',{'Graduate_boards':Graduate_boards})

### 소모임 게시판
def club_board(request):
    Club_boards = Club_board.objects.all()
    return render(request, 'club.html',{'Club_boards':Club_boards})

# 중고 서적 게시판
def market_board(request):
    Market_boards = Market_board.objects.all()
    return render(request, 'club.html',{'Market_boards':Market_boards})