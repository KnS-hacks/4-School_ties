from django.db import models

# Create your models here.
# 공지 게시판(공지 게시판 데이터 쌓이는 곳)
class Notice(models.Model) :
    Notice_title = models.CharField(max_length=2000)
    Notice_author = models.ForeignKey('account.User', on_delete = models.CASCADE)
    Notice_pub_date = models.DateField()
    Notice_body = models.TextField()
    Notice_image = models.ImageField(upload_to = "notice/", blank=True, null=True)

    def __str__(self):
        return self.Notice_title

# 공지 게시판 댓글
class Notice_Comment(models.Model):
    notice_content = models.CharField(max_length=500)
    notice_author = models.ForeignKey('account.User', on_delete = models.CASCADE)
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE, related_name="comments" )
    notice_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.notice_content

# 자유 게시판
class Free_board(models.Model) :
    Free_title = models.CharField(max_length=2000)
    Free_author = models.ForeignKey('account.User', on_delete = models.CASCADE)
    Free_pub_date = models.DateField()
    Free_body = models.TextField()
    Free_image = models.ImageField(upload_to = "Free_board/", blank=True, null=True)

    def __str__(self):
        return self.Free_title

# 자유 게시판 댓글
class Free_Comment(models.Model):
    free_content = models.CharField(max_length=500)
    free_author = models.ForeignKey('account.User', on_delete = models.CASCADE)
    free = models.ForeignKey(Free_board, on_delete=models.CASCADE, related_name="comments" )
    free_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.free_content

# 스터디 게시판
class Study_board(models.Model) :
    Study_title = models.CharField(max_length=2000)
    Study_author = models.ForeignKey('account.User', on_delete = models.CASCADE)
    Study_pub_date = models.DateField()
    Study_body = models.TextField()
    Study_image = models.ImageField(upload_to = "Study_board/", blank=True, null=True)

    def __str__(self):
        return self.Study_title

# 스터디 게시판 댓글
class Study_Comment(models.Model):
    study_content = models.CharField(max_length=500)
    study_author = models.ForeignKey('account.User', on_delete = models.CASCADE)
    study = models.ForeignKey(Study_board, on_delete=models.CASCADE, related_name="comments" )
    study_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.study_content

# 공모전 게시판
class Contest_board(models.Model) :
    Contest_title = models.CharField(max_length=2000)
    Contest_author = models.ForeignKey('account.User', on_delete = models.CASCADE)
    Contest_pub_date = models.DateField()
    Contest_body = models.TextField()
    Contest_image = models.ImageField(upload_to = "Contest_board/", blank=True, null=True)

    def __str__(self):
        return self.Contest_title

# 공모전 게시판 댓글
class Contest_Comment(models.Model):
    contest_content = models.CharField(max_length=500)
    contest_author = models.ForeignKey('account.User', on_delete = models.CASCADE)
    contest = models.ForeignKey(Contest_board, on_delete=models.CASCADE, related_name="comments" )
    contest_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.contest_content

# 졸업생 게시판
class Graduate_board(models.Model) :
    Graduate_title = models.CharField(max_length=2000)
    Graduate_author = models.ForeignKey('account.User', on_delete = models.CASCADE)
    Graduate_pub_date = models.DateField()
    Graduate_body = models.TextField()
    Graduate_image = models.ImageField(upload_to = "Graduate_board/", blank=True, null=True)

    def __str__(self):
        return self.Graduate_title

# 졸업생 게시판 댓글
class Graduate_Comment(models.Model):
    graduate_content = models.CharField(max_length=500)
    graduate_author = models.ForeignKey('account.User', on_delete = models.CASCADE)
    graduate = models.ForeignKey(Graduate_board, on_delete=models.CASCADE, related_name="comments" )
    graduate_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.graduate_content

# 동아리 게시판
class Club_board(models.Model) :
    Club_title = models.CharField(max_length=2000)
    Club_author = models.ForeignKey('account.User', on_delete = models.CASCADE)
    Club_pub_date = models.DateField()
    Club_body = models.TextField()
    Club_image = models.ImageField(upload_to = "Club_board/", blank=True, null=True)

    def __str__(self):
        return self.Club_title

# 동아리 게시판 댓글
class Club_Comment(models.Model):
    club_content = models.CharField(max_length=500)
    club_author = models.ForeignKey('account.User', on_delete = models.CASCADE)
    club = models.ForeignKey(Club_board, on_delete=models.CASCADE, related_name="comments" )
    club_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.club_content

# 중고 서적 게시판
class Market_board(models.Model) :
    Market_title = models.CharField(max_length=2000)
    Market_author = models.ForeignKey('account.User', on_delete = models.CASCADE)
    Market_pub_date = models.DateField()
    Market_body = models.TextField()
    Market_image = models.ImageField(upload_to = "Market_board/", blank=True, null=True)

    def __str__(self):
        return self.Market_title

# 중고 서적 게시판 댓글
class Market_Comment(models.Model):
    market_content = models.CharField(max_length=500)
    market_author =models.ForeignKey('account.User', on_delete = models.CASCADE)
    market = models.ForeignKey(Market_board, on_delete=models.CASCADE, related_name="comments" )
    market_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.market_content