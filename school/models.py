from django.db import models

# Create your models here.
# notice CRUD
class Notice(models.Model) :
    Notice_title = models.CharField(max_length=2000)
    Notice_author = models.CharField(max_length=50)
    Notice_pub_date = models.DateField()
    Notice_body = models.TextField()
    Notice_image = models.ImageField(upload_to = "notice/", blank=True, null=True)

    def __str__(self):
        return self.Notice_title

class Free_board(models.Model) :
    Free_title = models.CharField(max_length=2000)
    Free_author = models.CharField(max_length=50)
    Free_pub_date = models.DateField()
    Free_body = models.TextField()
    Free_image = models.ImageField(upload_to = "Free_board/", blank=True, null=True)

    def __str__(self):
        return self.Free_title

class Study_board(models.Model) :
    Study_title = models.CharField(max_length=2000)
    Study_author = models.CharField(max_length=50)
    Study_pub_date = models.DateField()
    Study_body = models.TextField()
    Study_image = models.ImageField(upload_to = "Study_board/", blank=True, null=True)

    def __str__(self):
        return self.Study_title

class Contest_board(models.Model) :
    Contest_title = models.CharField(max_length=2000)
    Contest_author = models.CharField(max_length=50)
    Contest_pub_date = models.DateField()
    Contest_body = models.TextField()
    Contest_image = models.ImageField(upload_to = "Contest_board/", blank=True, null=True)

    def __str__(self):
        return self.Contest_title

class Graduate_board(models.Model) :
    Graduate_title = models.CharField(max_length=2000)
    Graduate_author = models.CharField(max_length=50)
    Graduate_pub_date = models.DateField()
    Graduate_body = models.TextField()
    Graduate_image = models.ImageField(upload_to = "Graduate_board/", blank=True, null=True)

    def __str__(self):
        return self.Graduate_title

class Club_board(models.Model) :
    Club_title = models.CharField(max_length=2000)
    Club_author = models.CharField(max_length=50)
    Club_pub_date = models.DateField()
    Club_body = models.TextField()
    Club_image = models.ImageField(upload_to = "Graduate_board/", blank=True, null=True)

    def __str__(self):
        return self.Club_title

class Market_board(models.Model) :
    Market_title = models.CharField(max_length=2000)
    Market_author = models.CharField(max_length=50)
    Market_pub_date = models.DateField()
    Market_body = models.TextField()
    Market_image = models.ImageField(upload_to = "Graduate_board/", blank=True, null=True)

    def __str__(self):
        return self.Market_title