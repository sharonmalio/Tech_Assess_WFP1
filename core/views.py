from django_filters import rest_framework as filters
from rest_framework import viewsets

from .filters import DataFilter
from .models import WHOLifeExpectancy
from .serializers import DataSerializer


class DataViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows data to be viewed.
    """
    queryset = WHOLifeExpectancy.objects.filter(
        sex__in=['Male', 'Female'],
        GHO__in=[
            'Life expectancy at age 60 (years)',
            'Life expectancy at birth (years)'
        ]
    ).order_by('region')
    serializer_class = DataSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DataFilter