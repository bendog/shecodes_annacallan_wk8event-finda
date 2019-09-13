
import datetime

from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Event, Category

    
class NewEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'location', 'venue', 'start_time', 'end_time']
    # event_date = forms.DateTimeField(help_text="Enter a date and start time for the event")
    # event_title = forms.CharField(max_length=200, help_text ='Enter a title for your event')

        

    def clean_event_date(self):
        data = self.cleaned_data['start_time']
            
            # Check if a date is not in the past. 
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - event is in past'))

            # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=52):
            raise ValidationError(_('Invalid date - renewal more than 1 year ahead'))

            # Remember to always return the cleaned data.
        return data


    def save_new_event(request):
        form= NewEventForm(request.POST or None)
        if form.is_valid():
            form.save()
  
        context= {'form': form }
        return render(request, 'index.html', context)