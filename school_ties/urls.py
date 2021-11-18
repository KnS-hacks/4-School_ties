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
    path('notice/', S.notice, name='notice'),
    path('notice/post/', S.notice_post, name='notice_post'),
    path('notice/notice_detail/<str:id>', S.notice_detail, name='notice_detail'),
    path('notice/notice_edit/<str:id>', S.notice_edit, name='notice_edit'),
    path('notice/notice_update/<str:id>', S.notice_update, name='notice_update'),
    path('notice/notice_delete/<str:id>', S.notice_delete, name='notice_delete'),
    path('create_notice_comment/<str:notice_id>', S.create_notice_comment, name='create_notice_comment'),
    path('notice/delete_comment/<int:id>/<int:comment_id>', S.delete_notice_comment, name = "delete_notice_comment"),
    path('notice/update_comment/<int:id>/<int:comment_id>', S.update_notice_comment, name = "update_notice_comment"),

    path('free/', S.free_board, name='free'),
    path('study/', S.study_board, name='study'),
    path('contest/', S.contest_board, name='contest'),
    path('graduate/', S.graduate_board, name='graduate'),
    path('club/', S.club_board, name='club'),
    path('market/', S.market_board, name='market'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
