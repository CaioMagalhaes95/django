# todo_app/filters.py

import django_filters
from .models import Task
from django.db import models

class TaskFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_by_all_fields')
    category = django_filters.ChoiceFilter(choices=Task.CATEGORY_CHOICES)
    test_count = django_filters.ChoiceFilter(choices=Task.TEST_COUNT_CHOICES)
    particulate = django_filters.BooleanFilter()    
    requested_test_count = django_filters.ChoiceFilter(choices=Task.TEST_COUNT_CHOICES)

    class Meta:
        model = Task
        
        fields = {
            'completed': ['exact'],
            'category': ['exact'],
            'particulate': ['exact'],
            'test_count': ['exact'],
            'requested_test_count': ['exact'],

        }

    def filter_by_all_fields(self, queryset, name, value):
        return queryset.filter(
            models.Q(title__icontains=value) | models.Q(description__icontains=value)
        )
