from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# 유저 커스텀 모델로 인해 자체 어드민 페이지 생성
@admin.register(User)

class CustomUserAdmin(UserAdmin):

    ''' User admin Custom '''

    fieldsets = (
        (None, {"fields": ("username", "password", "real_name", "email",
                           "uni_num", "status", "card", "approval","rank_count","is_staff")},),
    )
    

    list_display = (
        "username",
        "real_name",
        "email",
        "uni_num",
        "status",
        "card",
        "approval",
        "rank_count",
        "is_staff"
    )