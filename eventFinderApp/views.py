from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render
from .models import Event, Category
from .forms import NewEventForm
#from django.views.generic.edit import CreateView


class IndexView(generic.ListView):
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all()


class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'


class NewEventView(generic.CreateView):
    template_name ='eventFinderApp/event_adder.html'
    form_class = NewEventForm
    queryset = Event.objects.all()
    success_url = '/event-finder/thanks/'

def get_new_event(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
    # create a form instance and populate it with data from the request:
        form = NewEventForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
        return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = NewEventForm()

    return render(request, 'eventFinderApp/event_adder.html', {'form': form})


def account(request):
    return render(request, 'eventFinderApp/account.html')

def thanks(request):
    return render(request, 'eventFinderApp/thanks.html')