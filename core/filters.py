from django.db import models
from django_filters import rest_framework as filters

from .models import WHOLifeExpectancy


class DataFilter(filters.FilterSet):
    """Filter set for data filtering."""
    class Meta:
        model = WHOLifeExpectancy
        fields = {
            'region': ['exact'],
            'GHO': ['exact'],
            'sex': ['exact'],
            'number_of_years': ['lte', 'gte'],
            'year': ['lte', 'gte']
        }
        filter_overrides = {
            models.CharField: {
                'filter_class': filters.CharFilter,
                'extra': lambda f: {
                    #pattern
                    'lookup_expr': 'icontains',
                },
            }
        }
