from django.db import models
# Create your models here.

class PublicBlogModel(models.Model):

    username = models.CharField(max_length=264)

    description = models.CharField(max_length=264, blank=False)

    pic = models.ImageField(upload_to = 'pics')

    blog =  models.TextField()

    def __str__(self):

        return self.username

class PrivateBlogModel(models.Model):

    username = models.CharField(max_length=264)

    description = models.CharField(max_length=264, blank=False)

    pic = models.ImageField(upload_to= 'pics')

    blog = models.TextField()

    def __str__(self):

        return self.username
