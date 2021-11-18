from django.db import models
from django.contrib.auth.models import AbstractUser

approval_ok = "승인완료"
approval_wait = "승인대기"
approval_choice = ((approval_ok, "승인완료"), (approval_wait, "승인대기"))
# Create your models here.
class User(AbstractUser):
    real_name = models.CharField(max_length=30, default="이름")
    email = models.EmailField(max_length=128)
    uni_num = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    card = models.ImageField(upload_to = "account/", blank=False, null=False)
    approval = models.CharField(
        choices = approval_choice, max_length = 10, null = False, blank = False, default="승인대기"
    )
    rank_count =  models.IntegerField(default=0, verbose_name = "board_score")