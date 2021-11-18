from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from django.utils import timezone
# Create your views here.
def home(request):
    return render(request, 'home.html')

### 공지사항
def notice(request):
    Notices = Notice.objects.all()
    return render(request, 'notice.html',{'Notices':Notices})

## 시작화면 주소##
def start(request):
    return render(request, 'start.html')

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
        return redirect('notice')
    else:
        return render(request, 'notice_new.html')

#공지사항 detail
def notice_detail(request, id):
    detail_notice = get_object_or_404(Notice, pk = id)
    print(detail_notice)
    return render(request, 'notice_detail.html', {'detail_notice':detail_notice})

#공지사항 update
def notice_edit(request, id):
    notice = Notice.objects.get(id = id)
    return render(request, 'notice_edit.html', {'notice': notice})

def notice_update(request, id):
    notice_update = Notice.objects.get(id = id)
    notice_update.Notice_title = request.POST['title']
    notice_update.Notice_author = request.POST['author']
    notice_update.Notice_image = request.FILES.get('image')
    notice_update.Notice_body = request.POST['body']
    notice_update.Notice_pub_date = timezone.now()
    notice_update.save()
    return redirect('notice_detail', notice_update.id)

#공지사항 삭제
def notice_delete(request, id):
    notice_delete = Notice.objects.get(id = id)
    notice_delete.delete()
    return redirect('notice')

#****공지사항 댓글*******
def create_notice_comment(request, notice_id):
    if request.method == 'POST':
        notice_comment = Notice_Comment()
        notice_comment.notice = get_object_or_404(Notice, pk=notice_id)
        notice_comment.notice_author = request.POST['author']
        notice_comment.notice_content = request.POST['content']
        notice_comment.notice_at = timezone.datetime.now()
        notice_comment.save()
        return redirect('notice_detail', notice_id)

# 공지사항 댓글 delete
def delete_notice_comment(request, id, comment_id):
    delete_notice_comment = Notice_Comment.objects.get(pk = comment_id)
    delete_notice_comment.delete()
    return redirect('notice_detail', id)

# 공지사항 댓글 update
def update_notice_comment(request, id, comment_id):
    if request.method == 'POST':
        update_notice_comment = get_object_or_404(Notice_Comment, pk=comment_id)
        update_notice_comment.notice_author = request.POST['author']
        update_notice_comment.notice_content = request.POST['content']
        update_notice_comment.save()
        return redirect('notice_detail', id)
    else:
        notice = get_object_or_404(Notice, pk=id)
        comment = get_object_or_404(Notice_Comment, pk=comment_id)
        return render(request, 'notice_comment_edit.html', {'notice':notice, 'comment':comment})  


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