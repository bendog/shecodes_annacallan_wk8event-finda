from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  # add additional fields in here
  events_attending = models.ManyToManyField(eventFinderApp.Event)



  def __str__(self):
    return self.email


