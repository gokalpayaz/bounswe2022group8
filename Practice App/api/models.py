from datetime import datetime
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Django creates an automatic id field: https://stackoverflow.com/a/35770315/16530078

class myUser(models.Model):
    # Built-in User has username and password already.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)  # EmailField is a CharField that checks the value for a valid email address using EmailValidator
    followers = models.ManyToManyField(User, related_name= "followed_by", blank=True)   # not required
    followed_users = models.ManyToManyField(User, related_name= "follows", blank=True)  # not required
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name + " " + self.surname 

class Tag(models.Model):
    tagname = models.CharField(max_length=100)
    description = models.CharField(max_length=500)  # description about the tag
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tagname

class ArtItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    owner = models.ForeignKey(myUser, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return "Art item: " + self.title

class Comment(models.Model):
    body = models.CharField(max_length=500)
    commented_by = models.ForeignKey(myUser, on_delete= models.CASCADE) 
    commented_on = models.ForeignKey(ArtItem, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


    def __str__(self):
        return "A comment made by " + str(self.commented_by) 

  
    

# Create your models here.