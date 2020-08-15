from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Image(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name = "images")
    url = models.CharField(max_length=200)


class AlbumPic(models.Model):
    url = models.CharField(max_length=200)
    





class Graduation(models.Model):
    start_time = models.DateTimeField(verbose_name="start_time")
    school = models.CharField(verbose_name="school", max_length=100)
    professional = models.CharField(verbose_name="professional", max_length=100)


class Experience(models.Model):
    start_time = models.DateTimeField(verbose_name="start_time")
    company = models.CharField(verbose_name="Company and work position", max_length=100)
    work_content = models.CharField(verbose_name="work_content", max_length=100)
