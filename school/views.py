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

#공지사항 delete
def notice_delete(request, id):
    notice_delete = Notice.objects.get(id = id)
    notice_delete.delete()
    return redirect('notice')

# 공지사항 댓글 create
def notice_comment_c(request, id):
    if request.method == 'POST':
        Noc = No_comment()
        Noc.notice = get_object_or_404(Notice, pk = id)
        Noc.Noc_author = request.POST['author']
        Noc.Noc_content = request.POST['content']
        Noc.Noc_time = timezone.datetime.now()
        Noc.save()
        return redirect('notice_detail', id)

# 공지사항 댓글 delete
def notice_comment_d(request, id, comment_id):
    my_Noc = No_comment.objects.get(pk = comment_id)
    my_Noc.delete()
    return redirect('notice_detail', id)

# 공지사항 댓글 update
def notice_comment_u(request, id, comment_id):
    if request.method == 'POST':
        up_Noc = get_object_or_404(No_comment, pk=comment_id)
        up_Noc.Noc_author = request.POST['author']
        up_Noc.Noc_content = request.POST['content']
        up_Noc.save()
        return redirect('notice_detail', id)
    else:
        notice = get_object_or_404(Notice, pk=id)
        comment = get_object_or_404(No_comment, pk=comment_id)
        return render(request, 'notice_comment_edit.html', {'notice':notice, 'comment':comment})  


### 자유게시판
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