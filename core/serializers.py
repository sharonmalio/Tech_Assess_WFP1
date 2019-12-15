from rest_framework import serializers

from .models import WHOLifeExpectancy


class DataSerializer(serializers.ModelSerializer):
    """Serializer for WHO data."""

    class Meta:
        model = WHOLifeExpectancy
        fields = ('GHO', 'region', 'year', 'sex', 'number_of_years')
        # read_only_fields = ('GHO', 'region', 'year', 'sex', 'number_of_years')
