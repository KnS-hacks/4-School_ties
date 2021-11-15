from django.db import models

# Create your models here.
# notice CRUD
class Notice(models.Model) :
    title = models.CharField(max_length=2000)
    author = models.CharField(max_length=50)
    pub_date = models.DateField()
    body = models.TextField()
    notice_image = models.ImageField(upload_to = "notice/", blank=True, null=True)

    def __str__(self):
        return self.title