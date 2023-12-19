from django.db import models
from django.contrib.auth.models import User


"""User class is bultin,that has some fixed attribute. But we need some extra attribute
that's why below class will contains extras,and  connected with User class"""
class UserProfile(models.Model):
    #this user will help yo connect with User class
    user=models.OneToOneField(User,related_name='user_profile',on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pics')
    dob=models.DateField(null=True)
    description = models.TextField(blank=True)
    city=models.CharField(null=True,max_length=15)
    bio=models.CharField(null=True,max_length=50)

    def __str__(self):
     return self.user.username
    

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    created_date = models.DateTimeField(auto_now_add=True)