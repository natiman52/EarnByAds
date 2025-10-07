from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **kwargs):
        
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class MyUser(AbstractUser):
    username = models.CharField(max_length=225,unique=True)
    earned = models.FloatField(default=0.00)
    ads_watched = models.IntegerField(default=0)
    objects = UserManager()
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username