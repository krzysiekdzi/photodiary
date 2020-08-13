from django.db import models

# Create your models here.

class Diary(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default = '')

class PhotoObject(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now=True)
    filePath = models.CharField(max_length=50)
    diary = models.ForeignKey(Diary, related_name = 'diary', on_delete = models.CASCADE, default = None)

class Comment(models.Model):
    author = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now=True)
    text = models.TextField(default = '')
    photo = models.ForeignKey(PhotoObject, on_delete=models.CASCADE)