from django.db import models

# Create your models here.
# 1. notice CRUD
class Notice(models.Model) :
    Notice_title = models.CharField(max_length=2000)
    Notice_author = models.CharField(max_length=50)
    Notice_pub_date = models.DateField()
    Notice_body = models.TextField()
    Notice_image = models.ImageField(upload_to = "notice/", blank=True, null=True)

    def __str__(self):
        return self.Notice_title

class No_comment(models.Model) :
    Noc_content = models.CharField(max_length=2000)
    Noc_author = models.CharField(max_length=50)
    notice = models.ForeignKey(Notice, on_delete = models.CASCADE)
    Noc_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.Noc_content

# 2. 자유게시판
class Free_board(models.Model) :
    Free_title = models.CharField(max_length=2000)
    Free_author = models.CharField(max_length=50)
    Free_pub_date = models.DateField()
    Free_body = models.TextField()
    Free_image = models.ImageField(upload_to = "Free_board/", blank=True, null=True)

    def __str__(self):
        return self.Free_title


class Fr_comment(models.Model) :
    Frc_content = models.CharField(max_length=2000)
    Frc_author = models.CharField(max_length=50)
    free = models.ForeignKey(Notice, on_delete = models.CASCADE)
    Frc_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.Frc_content

# 3. 스터티보드
class Study_board(models.Model) :
    Study_title = models.CharField(max_length=2000)
    Study_author = models.CharField(max_length=50)
    Study_pub_date = models.DateField()
    Study_body = models.TextField()
    Study_image = models.ImageField(upload_to = "Study_board/", blank=True, null=True)

    def __str__(self):
        return self.Study_title

class St_comment(models.Model) :
    Stc_content = models.CharField(max_length=2000)
    Stc_author = models.CharField(max_length=50)
    study = models.ForeignKey(Notice, on_delete = models.CASCADE)
    Stc_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.Stc_content

# 4. 공모전 게시판
class Contest_board(models.Model) :
    Contest_title = models.CharField(max_length=2000)
    Contest_author = models.CharField(max_length=50)
    Contest_pub_date = models.DateField()
    Contest_body = models.TextField()
    Contest_image = models.ImageField(upload_to = "Contest_board/", blank=True, null=True)

    def __str__(self):
        return self.Contest_title

class Co_comment(models.Model) :
    Coc_content = models.CharField(max_length=2000)
    Coc_author = models.CharField(max_length=50)
    contest = models.ForeignKey(Notice, on_delete = models.CASCADE)
    Coc_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.Coc_content

# 5. 졸업생 게시판
class Graduate_board(models.Model) :
    Graduate_title = models.CharField(max_length=2000)
    Graduate_author = models.CharField(max_length=50)
    Graduate_pub_date = models.DateField()
    Graduate_body = models.TextField()
    Graduate_image = models.ImageField(upload_to = "Graduate_board/", blank=True, null=True)

    def __str__(self):
        return self.Graduate_title

class Gr_comment(models.Model) :
    Grc_content = models.CharField(max_length=2000)
    Grc_author = models.CharField(max_length=50)
    graduate = models.ForeignKey(Notice, on_delete = models.CASCADE)
    Grc_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.Grc_content

# 6. club 게시판
class Club_board(models.Model) :
    Club_title = models.CharField(max_length=2000)
    Club_author = models.CharField(max_length=50)
    Club_pub_date = models.DateField()
    Club_body = models.TextField()
    Club_image = models.ImageField(upload_to = "Graduate_board/", blank=True, null=True)

    def __str__(self):
        return self.Club_title

class Cl_comment(models.Model) :
    Clc_content = models.CharField(max_length=2000)
    Clc_author = models.CharField(max_length=50)
    club = models.ForeignKey(Notice, on_delete = models.CASCADE)
    Clc_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.Clc_content

# 7. 중고거래 게시판
class Market_board(models.Model) :
    Market_title = models.CharField(max_length=2000)
    Market_author = models.CharField(max_length=50)
    Market_pub_date = models.DateField()
    Market_body = models.TextField()
    Market_image = models.ImageField(upload_to = "Graduate_board/", blank=True, null=True)

    def __str__(self):
        return self.Market_title

class Ma_comment(models.Model) :
    Mac_content = models.CharField(max_length=2000)
    Mac_author = models.CharField(max_length=50)
    market = models.ForeignKey(Notice, on_delete = models.CASCADE)
    Mac_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.Mac_content