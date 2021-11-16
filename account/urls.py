from django.urls import path
from . import views as A
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('login/', A.login, name = "login"),
    path('logout/', A.logout, name = "logout"),
    path('signup/', A.signup, name = "signup"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)