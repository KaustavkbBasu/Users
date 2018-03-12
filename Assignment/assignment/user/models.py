from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Users(models.Model):
    user_id = models.IntegerField(primary_key=True,default=0)
    user_name = models.CharField(max_length=200)
    First_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    place_of_birth = models.CharField(max_length=200)
    current_address = models.CharField(max_length=200)
    favourite_colour = models.CharField(max_length=200)
    personal_interest = models.CharField(max_length=200)
    my_friend = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return reverse("user_detail",kwargs={'pk':self.user_id})

class Friend(models.Model):
    users = models.ForeignKey('user.Users',related_name="us")

    def get_absolute_url(self):
        return reverse("user_list")
