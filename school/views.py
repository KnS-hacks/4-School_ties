from django.core import paginator
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from django.utils import timezone
from account.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    notices = Notice.objects.all().order_by('-Notice_pub_date')
    paginator = Paginator(notices, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'home.html',{'notices':page})

## 메인 자유게시판
def mainpage(requset):
    return render(requset, 'mainpage.html')

## 시작화면 주소 ##
def start(request):
    return render(request, 'start.html')

### 공지사항
@login_required
def notice(request):
    Notices = Notice.objects.all().order_by('-Notice_pub_date')
    paginator = Paginator(Notices, 2)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'notice.html',{'Notices':page})

# 공지사항 create
@login_required
@staff_member_required
def notice_post(request):
    if request.method == 'POST':
        new_notice = Notice()
        user_id = request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값. 즉 글 작성자의 user 객체를 user 변수에 저장합니다. 
        user = User.objects.get(id = user_id)
        print(user)
        # 작성자 = user 가 됩니다. 
        new_notice.Notice_title = request.POST['title']
        new_notice.Notice_author = user
        new_notice.Notice_image = request.FILES.get('image')
        new_notice.Notice_body = request.POST['body']
        new_notice.Notice_pub_date = timezone.now()
        user_id = request.user.id
        new_notice.save()
        save_score = User.objects.get(id = user_id)
        save_score.rank_count += 1
        save_score.save()
        return redirect('notice')
    else:
        return render(request, 'notice_new.html')

#공지사항 
@login_required
def notice_detail(request, id):
    detail_notice = get_object_or_404(Notice, pk = id)
    print(detail_notice)
    return render(request, 'notice_detail.html', {'detail_notice':detail_notice})

#공지사항 update
@login_required
@staff_member_required
def notice_edit(request, id):
    notice = Notice.objects.get(id = id)
    return render(request, 'notice_edit.html', {'notice': notice})

def notice_update(request, id):
    notice_update = Notice.objects.get(id = id)
    user_id = request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값. 즉 글 작성자의 user 객체를 user 변수에 저장합니다. 
    user = User.objects.get(id = user_id)    
    notice_update.Notice_title = request.POST['title']
    notice_update.Notice_author = user
    notice_update.Notice_image = request.FILES.get('image')
    notice_update.Notice_body = request.POST['body']
    notice_update.Notice_pub_date = timezone.now()
    notice_update.save()
    return redirect('notice_detail', notice_update.id)

#공지사항 삭제
@login_required
@staff_member_required
def notice_delete(request, id):
    notice_delete = Notice.objects.get(id = id)
    user_id = request.user.id
    save_score = User.objects.get(id = user_id)
    save_score.rank_count -= 1
    save_score.save()
    notice_delete.delete()
    return redirect('notice')

#****공지사항 댓글*******
@login_required
def create_notice_comment(request, notice_id):
    if request.method == 'POST':
        notice_comment = Notice_Comment()
        user_id = request.user.id
        user = User.objects.get(id = user_id)
        print(user)
        # 작성자 = user 가 됩니다. 
        notice_comment.notice = get_object_or_404(Notice, pk=notice_id)
        notice_comment.notice_author = user
        notice_comment.notice_content = request.POST['content']
        notice_comment.notice_at = timezone.datetime.now()
        notice_comment.save()
        return redirect('notice_detail', notice_id)

# 공지사항 댓글 delete
@login_required
def delete_notice_comment(request, id, comment_id):
    delete_notice_comment = Notice_Comment.objects.get(pk = comment_id)
    delete_notice_comment.delete()
    return redirect('notice_detail', id)

# 공지사항 댓글 update
@login_required
def update_notice_comment(request, id, comment_id):
    if request.method == 'POST':
        user_id = request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값. 즉 글 작성자의 user 객체를 user 변수에 저장합니다. 
        user = User.objects.get(id = user_id)
        update_notice_comment = get_object_or_404(Notice_Comment, pk=comment_id)
        update_notice_comment.notice_author = user
        update_notice_comment.notice_content = request.POST['content']
        update_notice_comment.save()
        return redirect('notice_detail', id)
    else:
        notice = get_object_or_404(Notice, pk=id)
        comment = get_object_or_404(Notice_Comment, pk=comment_id)
        return render(request, 'notice_comment_edit.html', {'notice':notice, 'comment':comment})  


### 자유게시판
@login_required
def free_board(request):
    Free_boards = Free_board.objects.all()
    return render(request, 'free.html',{'Free_boards':Free_boards})



### 스터디 게시판 
@login_required

def study_board(request):
    Study_boards = Study_board.objects.all()
    return render(request, 'study.html',{'Study_boards':Study_boards})

### 공모전 게시판
@login_required

def contest_board(request):
    Contest_boards = Contest_board.objects.all()
    return render(request, 'contest.html',{'Contest_boards':Contest_boards})

### 졸업생 게시판
@login_required
def graduate_board(request):
    Graduate_boards = Graduate_board.objects.all()
    return render(request, 'graduate.html',{'Graduate_boards':Graduate_boards})

### 소모임 게시판
@login_required
def club_board(request):
    Club_boards = Club_board.objects.all()
    return render(request, 'club.html',{'Club_boards':Club_boards})

### 중고 서적 게시판
@login_required
def market_board(request):
    Market_boards = Market_board.objects.all()
    return render(request, 'club.html',{'Market_boards':Market_boards})


### 게시판 랭킹
@login_required
def rank(request):
    rank = User.objects.filter(status = "학부생").order_by('-rank_count')
    return render(request, 'rank.html', {"rank":rank})