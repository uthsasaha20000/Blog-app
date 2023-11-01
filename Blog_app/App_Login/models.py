from django.db import models
from django.contrib.auth.models import User


"""User class is bultin,that has some fixed attribute. But we need some extra attribute
that's why below class will contains extras,and  connected with User class"""
class UserProfile(models.Model):
    #this user will help yo connect with User class
    user=models.OneToOneField(User,related_name='user_profile',on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pics')