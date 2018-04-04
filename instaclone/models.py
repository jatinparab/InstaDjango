from django.db import models


class User(models.Model):
    is_authenticated = True
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=120)
    last_login = models.DateTimeField(auto_now=True)
    profilepic = models.CharField(max_length=255,default='')

class Photo(models.Model):
    baseurl = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    date_uploaded = models.DateTimeField(auto_now=True)
    owner = models.CharField(max_length=20)
    likes = models.IntegerField()
    caption = models.CharField(max_length=140, default="")
    tags = models.IntegerField(default=0)
    main_colour = models.CharField(max_length=15, default="")

class PhotoTag(models.Model):
    photoid = models.IntegerField()
    coords = models.CharField(max_length=20)
    tagged_user = models.CharField(max_length=20, default="")
    tagged_by = models.CharField(max_length=20, default="")
