from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    venue = models.CharField(max_length=200, default = '')
    start_time = models.DateTimeField('start time and date')
    end_time = models.DateTimeField('end time and date')
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def category_names(self):
        all_names = ""
        for cat in self.categories.all():
            all_names = all_names + str(cat) + ", "
            
        if len(all_names)==0:
            return "categories unknown"
        
        return all_names[0:-2]



