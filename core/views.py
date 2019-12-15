from django_filters import rest_framework as filters
from rest_framework import viewsets

from .filters import DataFilter
from .models import WHOLifeExpectancy
from .serializers import DataSerializer

#not more posts
class DataViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows data to be viewed.
    """
    queryset = WHOLifeExpectancy.objects.all().order_by('region')
    serializer_class = DataSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DataFilter
