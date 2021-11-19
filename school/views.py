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

## 시작화면 주소
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

#공지사항 detail
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

#공지사항 delete
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



### 자유게시판 ###
@login_required
def free_board(request):
    Free_boards = Free_board.objects.all()
    return render(request, 'free.html',{'Free_boards':Free_boards})

# 자유게시판 create
@login_required
def free_post(request):
    if request.method == 'POST':
        new_free = Free_board()
        user_id = request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값. 즉 글 작성자의 user 객체를 user 변수에 저장합니다. 
        user = User.objects.get(id = user_id)
        print(user)
        # 작성자 = user 가 됩니다. 
        new_free.Free_title = request.POST['title']
        new_free.Free_author = user
        new_free.Free_image = request.FILES.get('image')
        new_free.Free_body = request.POST['body']
        new_free.Free_pub_date = timezone.now()
        user_id = request.user.id
        new_free.save()
        save_score = User.objects.get(id = user_id)
        save_score.rank_count += 1
        save_score.save()
        return redirect('free')
    else:
        return render(request, 'free_new.html')

#자유게시판 detail
@login_required
def free_detail(request, id):
    detail_free = get_object_or_404(Free_board, pk = id)
    print(detail_free)
    return render(request, 'free_detail.html', {'detail_free':detail_free})

#자유게시판 update
@login_required
def free_edit(request, id):
    free = Free_board.objects.get(id = id)
    return render(request, 'free_edit.html', {'free': free})

def free_update(request, id):
    free_update = Free_board.objects.get(id = id)
    user_id = request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값. 즉 글 작성자의 user 객체를 user 변수에 저장합니다. 
    user = User.objects.get(id = user_id)    
    free_update.Free_title = request.POST['title']
    free_update.Free_author = user
    free_update.Free_image = request.FILES.get('image')
    free_update.Free_body = request.POST['body']
    free_update.Free_pub_date = timezone.now()
    free_update.save()
    return redirect('free_detail', free_update.id)

#자유게시판 delete
@login_required
def free_delete(request, id):
    free_delete = Free_board.objects.get(id = id)
    user_id = request.user.id
    save_score = User.objects.get(id = user_id)
    save_score.rank_count -= 1
    save_score.save()
    free_delete.delete()
    return redirect('free')


#****자유게시판 댓글*******
@login_required
def create_free_comment(request, free_id):
    if request.method == 'POST':
        free_comment = Free_Comment()
        user_id = request.user.id
        user = User.objects.get(id = user_id)
        print(user)
        # 작성자 = user 가 됩니다. 
        free_comment.free = get_object_or_404(Free_board, pk=free_id)
        free_comment.free_author = user
        free_comment.free_content = request.POST['content']
        free_comment.free_at = timezone.datetime.now()
        free_comment.save()
        return redirect('free_detail', free_id)

# 자유게시판 댓글 delete
@login_required
def delete_free_comment(request, id, comment_id):
    delete_free_comment = Free_Comment.objects.get(pk = comment_id)
    delete_free_comment.delete()
    return redirect('free_detail', id)

# 자유게시판 댓글 update
@login_required
def update_free_comment(request, id, comment_id):
    if request.method == 'POST':
        user_id = request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값. 즉 글 작성자의 user 객체를 user 변수에 저장합니다. 
        user = User.objects.get(id = user_id)
        update_free_comment = get_object_or_404(Free_Comment, pk=comment_id)
        update_free_comment.free_author = user
        update_free_comment.free_content = request.POST['content']
        update_free_comment.save()
        return redirect('free_detail', id)
    else:
        free = get_object_or_404(Free_board, pk=id)
        comment = get_object_or_404(Free_Comment, pk=comment_id)
        return render(request, 'free_comment_edit.html', {'free':free, 'comment':comment})  



### 스터디 게시판 ###
@login_required
def study_board(request):
    Study_boards = Study_board.objects.all()
    return render(request, 'study.html',{'Study_boards':Study_boards})

# 스터디게시판 create
@login_required
def study_post(request):
    if request.method == 'POST':
        new_study = Study_board()
        user_id = request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값. 즉 글 작성자의 user 객체를 user 변수에 저장합니다. 
        user = User.objects.get(id = user_id)
        print(user)
        # 작성자 = user 가 됩니다. 
        new_study.Study_title = request.POST['title']
        new_study.Study_author = user
        new_study.Study_image = request.FILES.get('image')
        new_study.Study_body = request.POST['body']
        new_study.Study_pub_date = timezone.now()
        user_id = request.user.id
        new_study.save()
        save_score = User.objects.get(id = user_id)
        save_score.rank_count += 1
        save_score.save()
        return redirect('study')
    else:
        return render(request, 'study_new.html')

#스터디게시판 detail
@login_required
def study_detail(request, id):
    detail_notice = get_object_or_404(Notice, pk = id)
    print(detail_notice)
    return render(request, 'notice_detail.html', {'detail_notice':detail_notice})

#스터디게시판 update
@login_required
def study_edit(request, id):
    study = Study_board.objects.get(id = id)
    return render(request, 'study_edit.html', {'study': study})

def study_update(request, id):
    study_update = Study_board.objects.get(id = id)
    user_id = request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값. 즉 글 작성자의 user 객체를 user 변수에 저장합니다. 
    user = User.objects.get(id = user_id)    
    study_update.Study_title = request.POST['title']
    study_update.Study_author = user
    study_update.Study_image = request.FILES.get('image')
    study_update.Study_body = request.POST['body']
    study_update.Study_pub_date = timezone.now()
    study_update.save()
    return redirect('study_detail', study_update.id)

#스터디게시판 delete
@login_required
def study_delete(request, id):
    study_delete = Study_board.objects.get(id = id)
    user_id = request.user.id
    save_score = User.objects.get(id = user_id)
    save_score.rank_count -= 1
    save_score.save()
    study_delete.delete()
    return redirect('study')


#****스터디게시판 댓글*******
@login_required
def create_study_comment(request, study_id):
    if request.method == 'POST':
        study_comment = Study_Comment()
        user_id = request.user.id
        user = User.objects.get(id = user_id)
        print(user)
        # 작성자 = user 가 됩니다. 
        study_comment.study = get_object_or_404(Study_board, pk=study_id)
        study_comment.study_author = user
        study_comment.study_content = request.POST['content']
        study_comment.study_at = timezone.datetime.now()
        study_comment.save()
        return redirect('study_detail', study_id)

# 스터디 댓글 delete
@login_required
def delete_study_comment(request, id, comment_id):
    delete_study_comment = Study_Comment.objects.get(pk = comment_id)
    delete_study_comment.delete()
    return redirect('study_detail', id)

# 스터디 댓글 update
@login_required
def update_study_comment(request, id, comment_id):
    if request.method == 'POST':
        user_id = request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값. 즉 글 작성자의 user 객체를 user 변수에 저장합니다. 
        user = User.objects.get(id = user_id)
        update_study_comment = get_object_or_404(Study_Comment, pk=comment_id)
        update_study_comment.study_author = user
        update_study_comment.study_content = request.POST['content']
        update_study_comment.save()
        return redirect('study_detail', id)
    else:
        study = get_object_or_404(Study_board, pk=id)
        comment = get_object_or_404(Study_Comment, pk=comment_id)
        return render(request, 'study_comment_edit.html', {'study':study, 'comment':comment})  



### 공모전 게시판
@login_required
def contest_board(request):
    Contest_boards = Contest_board.objects.all()
    return render(request, 'contest.html',{'Contest_boards':Contest_boards})

# 공모전게시판 create
@login_required
def contest_post(request):
    if request.method == 'POST':
        new_contest = Contest_board()
        user_id = request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값. 즉 글 작성자의 user 객체를 user 변수에 저장합니다. 
        user = User.objects.get(id = user_id)
        print(user)
        # 작성자 = user 가 됩니다. 
        new_contest.Contest_title = request.POST['title']
        new_contest.Contest_author = user
        new_contest.Contest_image = request.FILES.get('image')
        new_contest.Contest_body = request.POST['body']
        new_contest.Contest_pub_date = timezone.now()
        user_id = request.user.id
        new_contest.save()
        save_score = User.objects.get(id = user_id)
        save_score.rank_count += 1
        save_score.save()
        return redirect('contest')
    else:
        return render(request, 'contest_new.html')

#공모전 detail
@login_required
def contest_detail(request, id):
    detail_contest = get_object_or_404(Contest_board, pk = id)
    print(detail_contest)
    return render(request, 'contest_detail.html', {'detail_contest':detail_contest})

#공모전 update
@login_required
def contest_edit(request, id):
    contest = Contest_board.objects.get(id = id)
    return render(request, 'contest_edit.html', {'contest': contest})

def contest_update(request, id):
    contest_update = Contest_board.objects.get(id = id)
    user_id = request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값. 즉 글 작성자의 user 객체를 user 변수에 저장합니다. 
    user = User.objects.get(id = user_id)    
    contest_update.Contest_title = request.POST['title']
    contest_update.Contest_author = user
    contest_update.Contest_image = request.FILES.get('image')
    contest_update.Contest_body = request.POST['body']
    contest_update.Contest_pub_date = timezone.now()
    contest_update.save()
    return redirect('contest_detail', contest_update.id)

#공모전 delete
@login_required
def contest_delete(request, id):
    contest_delete = Contest_board.objects.get(id = id)
    user_id = request.user.id
    save_score = User.objects.get(id = user_id)
    save_score.rank_count -= 1
    save_score.save()
    contest_delete.delete()
    return redirect('contest')


#****공지사항 댓글*******
@login_required
def create_contest_comment(request, contest_id):
    if request.method == 'POST':
        contest_comment = Contest_Comment()
        user_id = request.user.id
        user = User.objects.get(id = user_id)
        print(user)
        # 작성자 = user 가 됩니다. 
        contest_comment.contest = get_object_or_404(Contest_board, pk=contest_id)
        contest_comment.contest_author = user
        contest_comment.contest_content = request.POST['content']
        contest_comment.contest_at = timezone.datetime.now()
        contest_comment.save()
        return redirect('contest_detail', contest_id)

# 공지사항 댓글 delete
@login_required
def delete_contest_comment(request, id, comment_id):
    delete_contest_comment = Contest_Comment.objects.get(pk = comment_id)
    delete_contest_comment.delete()
    return redirect('contest_detail', id)

# 공지사항 댓글 update
@login_required
def update_contest_comment(request, id, comment_id):
    if request.method == 'POST':
        user_id = request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값. 즉 글 작성자의 user 객체를 user 변수에 저장합니다. 
        user = User.objects.get(id = user_id)
        update_contest_comment = get_object_or_404(Contest_Comment, pk=comment_id)
        update_contest_comment.contest_author = user
        update_contest_comment.contest_content = request.POST['content']
        update_contest_comment.save()
        return redirect('contest_detail', id)
    else:
        contest = get_object_or_404(Contest_board, pk=id)
        comment = get_object_or_404(Contest_Comment, pk=comment_id)
        return render(request, 'contest_comment_edit.html', {'contest':contest, 'comment':comment})  



### 졸업생 게시판
@login_required
def graduate_board(request):
    graduate_boards = Graduate_board.objects.all()
    return render(request, 'graduate.html',{'graduate_boards':graduate_boards})

# 졸업생게시판 create
@login_required
def graduate_post(request):
    if request.method == 'POST':
        new_graduate = Graduate_board()
        user_id = request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값. 즉 글 작성자의 user 객체를 user 변수에 저장합니다. 
        user = User.objects.get(id = user_id)
        print(user)
        # 작성자 = user 가 됩니다. 
        new_graduate.Graduate_title = request.POST['title']
        new_graduate.Graduate_author = user
        new_graduate.Graduate_image = request.FILES.get('image')
        new_graduate.Graduate_body = request.POST['body']
        new_graduate.Graduate_pub_date = timezone.now()
        user_id = request.user.id
        new_graduate.save()
        save_score = User.objects.get(id = user_id)
        save_score.rank_count += 1
        save_score.save()
        return redirect('graduate')
    else:
        return render(request, 'graduate_new.html')

# 졸업생게시판 detail
@login_required
def graduate_detail(request, id):
    detail_graduate = get_object_or_404(Graduate_board, pk = id)
    print(detail_graduate)
    return render(request, 'graduate_detail.html', {'detail_graduate':detail_graduate})

# 졸업생게시판 update
@login_required
def graduate_edit(request, id):
    graduate = Graduate_board.objects.get(id = id)
    return render(request, 'graduate_edit.html', {'graduate': graduate})

def graduate_update(request, id):
    graduate_update = Graduate_board.objects.get(id = id)
    user_id = request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값. 즉 글 작성자의 user 객체를 user 변수에 저장합니다. 
    user = User.objects.get(id = user_id)    
    graduate_update.Graduate_title = request.POST['title']
    graduate_update.Graduate_author = user
    graduate_update.Graduate_image = request.FILES.get('image')
    graduate_update.Graduate_body = request.POST['body']
    graduate_update.Graduate_pub_date = timezone.now()
    graduate_update.save()
    return redirect('graduate_detail', graduate_update.id)

# 졸업생게시판 delete
@login_required
def graduate_delete(request, id):
    graduate_delete = Graduate_board.objects.get(id = id)
    user_id = request.user.id
    save_score = User.objects.get(id = user_id)
    save_score.rank_count -= 1
    save_score.save()
    graduate_delete.delete()
    return redirect('graduate')


#****졸업생게시판 댓글*******
@login_required
def create_graduate_comment(request, graduate_id):
    if request.method == 'POST':
        graduate_comment = Graduate_Comment()
        user_id = request.user.id
        user = User.objects.get(id = user_id)
        print(user)
        # 작성자 = user 가 됩니다. 
        graduate_comment.graduate = get_object_or_404(Graduate_board, pk=graduate_id)
        graduate_comment.graduate_author = user
        graduate_comment.graduate_content = request.POST['content']
        graduate_comment.graduate_at = timezone.datetime.now()
        graduate_comment.save()
        return redirect('graduate_detail', graduate_id)

# 졸업생게시판 댓글 delete
@login_required
def delete_graduate_comment(request, id, comment_id):
    delete_graduate_comment = Graduate_Comment.objects.get(pk = comment_id)
    delete_graduate_comment.delete()
    return redirect('graduate_detail', id)

# 졸업생게시판 댓글 update
@login_required
def update_graduate_comment(request, id, comment_id):
    if request.method == 'POST':
        user_id = request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값. 즉 글 작성자의 user 객체를 user 변수에 저장합니다. 
        user = User.objects.get(id = user_id)
        update_graduate_comment = get_object_or_404(Graduate_Comment, pk=comment_id)
        update_graduate_comment.graduate_author = user
        update_graduate_comment.graduate_content = request.POST['content']
        update_graduate_comment.save()
        return redirect('graduate_detail', id)
    else:
        graduate = get_object_or_404(Graduate_board, pk=id)
        comment = get_object_or_404(Graduate_Comment, pk=comment_id)
        return render(request, 'graduate_comment_edit.html', {'graduate':graduate, 'comment':comment})  


### 동아리게시판
@login_required
def club_board(request):
    Club_boards = Club_board.objects.all()
    return render(request, 'club.html',{'Club_boards':Club_boards})

# 동아리게시판 create
@login_required
def club_post(request):
    if request.method == 'POST':
        new_club = Club_board()
        user_id = request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값. 즉 글 작성자의 user 객체를 user 변수에 저장합니다. 
        user = User.objects.get(id = user_id)
        print(user)
        # 작성자 = user 가 됩니다. 
        new_club.Club_title = request.POST['title']
        new_club.Club_author = user
        new_club.Club_image = request.FILES.get('image')
        new_club.Club_body = request.POST['body']
        new_club.Club_pub_date = timezone.now()
        user_id = request.user.id
        new_club.save()
        save_score = User.objects.get(id = user_id)
        save_score.rank_count += 1
        save_score.save()
        return redirect('club')
    else:
        return render(request, 'club_new.html')

# 동아리게시판 detail
@login_required
def club_detail(request, id):
    detail_club = get_object_or_404(Club_board, pk = id)
    print(detail_club)
    return render(request, 'club_detail.html', {'detail_club':detail_club})

#동아리게시판 update
@login_required
def club_edit(request, id):
    club = Club_board.objects.get(id = id)
    return render(request, 'club_edit.html', {'club': club})

def club_update(request, id):
    club_update = Club_board.objects.get(id = id)
    user_id = request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값. 즉 글 작성자의 user 객체를 user 변수에 저장합니다. 
    user = User.objects.get(id = user_id)    
    club_update.Club_title = request.POST['title']
    club_update.Club_author = user
    club_update.Club_image = request.FILES.get('image')
    club_update.Club_body = request.POST['body']
    club_update.Club_pub_date = timezone.now()
    club_update.save()
    return redirect('club_detail', club_update.id)

# 동아리게시판 delete
@login_required
def club_delete(request, id):
    club_delete = Club_board.objects.get(id = id)
    user_id = request.user.id
    save_score = User.objects.get(id = user_id)
    save_score.rank_count -= 1
    save_score.save()
    club_delete.delete()
    return redirect('club')


#****동아리게시판 댓글*******
@login_required
def create_club_comment(request, club_id):
    if request.method == 'POST':
        club_comment = Graduate_Comment()
        user_id = request.user.id
        user = User.objects.get(id = user_id)
        print(user)
        # 작성자 = user 가 됩니다. 
        club_comment.graduate = get_object_or_404(Club_board, pk=club_id)
        club_comment.graduate_author = user
        club_comment.graduate_content = request.POST['content']
        club_comment.graduate_at = timezone.datetime.now()
        club_comment.save()
        return redirect('club_detail', club_id)

# 동아리게시판 댓글 delete
@login_required
def delete_club_comment(request, id, comment_id):
    delete_club_comment = Club_Comment.objects.get(pk = comment_id)
    delete_club_comment.delete()
    return redirect('club_detail', id)

# 동아리게시판 댓글 update
@login_required
def update_club_comment(request, id, comment_id):
    if request.method == 'POST':
        user_id = request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값. 즉 글 작성자의 user 객체를 user 변수에 저장합니다. 
        user = User.objects.get(id = user_id)
        update_club_comment = get_object_or_404(Club_Comment, pk=comment_id)
        update_club_comment.club_author = user
        update_club_comment.club_content = request.POST['content']
        update_club_comment.save()
        return redirect('club_detail', id)
    else:
        club = get_object_or_404(Club_board, pk=id)
        comment = get_object_or_404(Club_Comment, pk=comment_id)
        return render(request, 'club_comment_edit.html', {'club':club, 'comment':comment})  


### 중고 서적 게시판
@login_required
def market_board(request):
    Market_boards = Market_board.objects.all()
    return render(request, 'market.html',{'Market_boards':Market_boards})


# 중고서적게시판 create
@login_required
def market_post(request):
    if request.method == 'POST':
        new_market = Market_board()
        user_id = request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값. 즉 글 작성자의 user 객체를 user 변수에 저장합니다. 
        user = User.objects.get(id = user_id)
        print(user)
        # 작성자 = user 가 됩니다. 
        new_market.Market_title = request.POST['title']
        new_market.Market_author = user
        new_market.Market_image = request.FILES.get('image')
        new_market.Market_body = request.POST['body']
        new_market.Market_pub_date = timezone.now()
        user_id = request.user.id
        new_market.save()
        save_score = User.objects.get(id = user_id)
        save_score.rank_count += 1
        save_score.save()
        return redirect('market')
    else:
        return render(request, 'market_new.html')

# 중고서적게시판 detail
@login_required
def market_detail(request, id):
    detail_market = get_object_or_404(Market_board, pk = id)
    print(detail_market)
    return render(request, 'market_detail.html', {'detail_market':detail_market})

# 중고서적게시판 update
@login_required
def market_edit(request, id):
    market = Market_board.objects.get(id = id)
    return render(request, 'market_edit.html', {'market': market})

def market_update(request, id):
    market_update = Market_board.objects.get(id = id)
    user_id = request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값. 즉 글 작성자의 user 객체를 user 변수에 저장합니다. 
    user = User.objects.get(id = user_id)    
    market_update.Market_title = request.POST['title']
    market_update.Market_author = user
    market_update.Market_image = request.FILES.get('image')
    market_update.Market_body = request.POST['body']
    market_update.Market_pub_date = timezone.now()
    market_update.save()
    return redirect('market_detail', market_update.id)

# 중고서적게시판 delete
@login_required
def market_delete(request, id):
    market_delete = Market_board.objects.get(id = id)
    user_id = request.user.id
    save_score = User.objects.get(id = user_id)
    save_score.rank_count -= 1
    save_score.save()
    market_delete.delete()
    return redirect('market')


#****중고서적게시판 댓글*******
@login_required
def create_market_comment(request, market_id):
    if request.method == 'POST':
        market_comment = Market_Comment()
        user_id = request.user.id
        user = User.objects.get(id = user_id)
        print(user)
        # 작성자 = user 가 됩니다. 
        market_comment.market = get_object_or_404(Market_board, pk=market_id)
        market_comment.market_author = user
        market_comment.market_content = request.POST['content']
        market_comment.market_at = timezone.datetime.now()
        market_comment.save()
        return redirect('graduate_detail', market_id)

# 중고서적게시판 댓글 delete
@login_required
def delete_market_comment(request, id, comment_id):
    delete_market_comment = Market_Comment.objects.get(pk = comment_id)
    delete_market_comment.delete()
    return redirect('market_detail', id)

# 중고서적게시판 댓글 update
@login_required
def update_market_comment(request, id, comment_id):
    if request.method == 'POST':
        user_id = request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값. 즉 글 작성자의 user 객체를 user 변수에 저장합니다. 
        user = User.objects.get(id = user_id)
        update_market_comment = get_object_or_404(Market_Comment, pk=comment_id)
        update_market_comment.market_author = user
        update_market_comment.market_content = request.POST['content']
        update_market_comment.save()
        return redirect('market_detail', id)
    else:
        market = get_object_or_404(Market_board, pk=id)
        comment = get_object_or_404(Market_Comment, pk=comment_id)
        return render(request, 'market_comment_edit.html', {'market':market, 'comment':comment})  



### 게시판 랭킹
# @login_required
def rank(request):
    rank = User.objects.filter(status = "학부생").order_by('-rank_count')
    return render(request, 'rank.html', {"rank":rank})