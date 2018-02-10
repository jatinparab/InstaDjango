from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=120)
    last_login = models.DateTimeField(auto_now=True)


