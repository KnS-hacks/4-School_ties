"""school_ties URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from school import views as S
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('home/', S.home, name='home'),
    path('',S.start, name="start"),
 #   path('boardform/',S.boardform, name="boardform"),
    path('notice/', S.notice, name='notice'),
    path('mainpage/',S.mainpage, name='mainpage'),
    path('notice/post/', S.notice_post, name='notice_post'),
    path('notice/notice_detail/<str:id>', S.notice_detail, name='notice_detail'),
    path('notice/notice_edit/<str:id>', S.notice_edit, name='notice_edit'),
    path('notice/notice_update/<str:id>', S.notice_update, name='notice_update'),
    path('notice/notice_delete/<str:id>', S.notice_delete, name='notice_delete'),
    path('create_notice_comment/<str:notice_id>', S.create_notice_comment, name='create_notice_comment'),
    path('notice/delete_comment/<int:id>/<int:comment_id>', S.delete_notice_comment, name = "delete_notice_comment"),
    path('notice/update_comment/<int:id>/<int:comment_id>', S.update_notice_comment, name = "update_notice_comment"),

    path('free/', S.free_board, name='free'),
    path('free/post/', S.free_post, name='free_post'),
    path('free/free_detail/<str:id>', S.free_detail, name='free_detail'),
    path('free/free_edit/<str:id>', S.free_edit, name='free_edit'),
    path('free/free_update/<str:id>', S.free_update, name='free_update'),
    path('free/free_delete/<str:id>', S.free_delete, name='free_delete'),
    path('create_free_comment/<str:free_id>', S.create_free_comment, name='create_free_comment'),
    path('free/delete_comment/<int:id>/<int:comment_id>', S.delete_free_comment, name = "delete_free_comment"),
    path('free/update_comment/<int:id>/<int:comment_id>', S.update_free_comment, name = "update_free_comment"),

    path('study/', S.study_board, name='study'),
    path('study/post/', S.study_post, name='study_post'),
    path('study/study_detail/<str:id>', S.study_detail, name='study_detail'),
    path('study/study_edit/<str:id>', S.study_edit, name='study_edit'),
    path('study/study_update/<str:id>', S.study_update, name='study_update'),
    path('study/study_delete/<str:id>', S.study_delete, name='study_delete'),
    path('create_study_comment/<str:study_id>', S.create_study_comment, name='create_study_comment'),
    path('study/delete_comment/<int:id>/<int:comment_id>', S.delete_study_comment, name = "delete_study_comment"),
    path('study/update_comment/<int:id>/<int:comment_id>', S.update_study_comment, name = "update_study_comment"),

    path('contest/', S.contest_board, name='contest'),
    path('contest/post/', S.contest_post, name='contest_post'),
    path('contest/contest_detail/<str:id>', S.contest_detail, name='contest_detail'),
    path('contest/contest_edit/<str:id>', S.contest_edit, name='contest_edit'),
    path('contest/contest_update/<str:id>', S.contest_update, name='contest_update'),
    path('contest/contest_delete/<str:id>', S.contest_delete, name='contest_delete'),
    path('create_contest_comment/<str:contest_id>', S.create_contest_comment, name='create_contest_comment'),
    path('contest/delete_comment/<int:id>/<int:comment_id>', S.delete_contest_comment, name = "delete_contest_comment"),
    path('contest/update_comment/<int:id>/<int:comment_id>', S.update_contest_comment, name = "update_contest_comment"),

    path('graduate/', S.graduate_board, name='graduate'),
    path('graduate/post/', S.graduate_post, name='graduate_post'),
    path('graduate/graduate_detail/<str:id>', S.graduate_detail, name='graduate_detail'),
    path('graduate/graduate_edit/<str:id>', S.graduate_edit, name='graduate_edit'),
    path('graduate/graduate_update/<str:id>', S.graduate_update, name='graduate_update'),
    path('graduate/graduate_delete/<str:id>', S.graduate_delete, name='graduate_delete'),
    path('create_graduate_comment/<str:graduate_id>', S.create_graduate_comment, name='create_graduate_comment'),
    path('graduate/delete_comment/<int:id>/<int:comment_id>', S.delete_graduate_comment, name = "delete_graduate_comment"),
    path('graduate/update_comment/<int:id>/<int:comment_id>', S.update_graduate_comment, name = "update_graduate_comment"),

    path('club/', S.club_board, name='club'),
    path('club/post/', S.club_post, name='club_post'),
    path('club/club_detail/<str:id>', S.club_detail, name='club_detail'),
    path('club/club_edit/<str:id>', S.club_edit, name='club_edit'),
    path('club/club_update/<str:id>', S.club_update, name='club_update'),
    path('club/club_delete/<str:id>', S.club_delete, name='club_delete'),
    path('create_club_comment/<str:club_id>', S.create_club_comment, name='create_club_comment'),
    path('club/delete_comment/<int:id>/<int:comment_id>', S.delete_club_comment, name = "delete_club_comment"),
    path('club/update_comment/<int:id>/<int:comment_id>', S.update_club_comment, name = "update_club_comment"),

    path('market/', S.market_board, name='market'),
    path('market/post/', S.market_post, name='market_post'),
    path('market/market_detail/<str:id>', S.market_detail, name='market_detail'),
    path('market/market_edit/<str:id>', S.market_edit, name='market_edit'),
    path('market/market_update/<str:id>', S.market_update, name='market_update'),
    path('market/market_delete/<str:id>', S.market_delete, name='market_delete'),
    path('create_market_comment/<str:market_id>', S.create_market_comment, name='create_market_comment'),
    path('market/delete_comment/<int:id>/<int:comment_id>', S.delete_market_comment, name = "delete_market_comment"),
    path('market/update_comment/<int:id>/<int:comment_id>', S.update_market_comment, name = "update_market_comment"),

    path('rank/', S.rank, name="rank"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
