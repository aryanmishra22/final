from django.db import models

# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length=256, null=False, blank=False)
    lname = models.CharField(max_length=256, null=False, blank=False)
    username = models.CharField(max_length=256, null=False, blank=False)