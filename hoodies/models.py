from django.shortcuts import render,redirect
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
import datetime as dt
from django.shortcuts import get_object_or_404
# Create your models here.


class Location(models.Model):
    city = models.CharField(max_length=30, blank=True)
    hood = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.hoodies

class NeighbourHood (models.Model):
    user_id = models.ForeignKey(User,blank=True, on_delete=models.CASCADE,related_name='user',null=True)
    hood_name = models.CharField(max_length=30, blank=True)
    location_id = models.ForeignKey(Location,blank=True, on_delete=models.CASCADE,related_name='location',null=True)

    def __str__(self):
        return self.hood_name


class Business(models.Model):
    business_name = models.CharField(max_length=30, blank=True)
    user = models.ForeignKey(User,blank=True, on_delete=models.CASCADE,related_name='neighborhood',null=True)
    neighborhood_id = models.ForeignKey(NeighbourHood,blank=True, on_delete=models.CASCADE,related_name='neighborhood',null=True)
    business_email = models.EmailField(max_length=70,blank=True)
    image_path = models.ImageField(upload_to = 'gallery/')
    def __str__(self):
        return self.business_name


class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
    name = models.CharField(max_length=30, blank=True)
    email_address = models.EmailField(max_length=70,blank=True)
    neighborhood_id = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE,related_name="profile_hood",null=True)
    def __str__(self):
        return self.name
        class Meta:
            ordering= ['user']

    def save_user(self):
        self.save()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender,instance, **kwargs):
        instance.profile.save()

class Post(models.Model):

    image_path = models.ImageField(upload_to = 'gallery/')
    image_description = models.CharField(max_length=100, blank=True)
    hood_id = models.ForeignKey(NeighbourHood,null=True)


class Activities(models.Model):
    name = models.CharField(max_length=30, blank=True)
    user = models.ForeignKey(User,blank=True, on_delete=models.CASCADE)
    neigh = models.ForeignKey(NeighbourHood,blank=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=70,blank=True)
    path = models.ImageField(upload_to = 'gallery/')

    @classmethod
    def search_by_activity_name(cls,search_term):
        project = Activitiy.objects.filter(activity_name__icontains = search_term)
        return project