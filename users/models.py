from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
  # add additional fields in here
    events_attending = models.ManyToManyField('eventFinderApp.Event')
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100)



    def __str__(self):
        return self.email



    def get_events_attending(self):
        '''Return the events attending.'''
        your_events = ''
        for your_event in self.events_attending.all():
            your_events = your_event + str(your_event) + ','

        if len(your_events)==0:
            return "You have no upcoming events"
        
        return your_events[0:-2]