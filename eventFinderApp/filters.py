import django_filters
from .models import Event, Category


class EventFilter(django_filters.FilterSet):

    # CHOICES = (
    #     ('ascending', 'Ascending'),
    #     ('descending', 'Descending'),
    # )

    # ordering = django_filters.ChoiceFilter(label='Ordering', choices =CHOICES, method='filter_by_order')

    class Meta:
        model = Event
        fields = {"title": ["icontains"], "categories": ["exact"]}

    # def filter_by_order(self, queryset, name, value):
    #     expression = 'created' if value == 'ascending' else '-created'
    #     return queryset.order_by(expression)
