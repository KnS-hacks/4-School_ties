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
    path('', S.home, name='home'),
    path('notice/', S.notice, name='notice'),
    path('free/', S.free_board, name='free'),
    path('study/', S.study_board, name='study'),
    path('contest/', S.contest_board, name='contest'),
    path('graduate/', S.graduate_board, name='graduate'),
    path('club/', S.club_board, name='club'),
    path('market/', S.market_board, name='market'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
