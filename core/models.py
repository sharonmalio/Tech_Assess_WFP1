from django.db import models
from django.utils import timezone

from .constants import SEXES, WHO_REGIONS

# data structure object

class WHOLifeExpectancy(models.Model):
    """Model to store WHO data on life expectancy."""
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    GHO = models.CharField(max_length=100)
    region = models.CharField(max_length=30, choices=WHO_REGIONS)
    year = models.PositiveIntegerField(default=timezone.now().year)
    sex = models.CharField(max_length=10, choices=SEXES)
    number_of_years = models.FloatField()

    class Meta:
        #unique entries
        unique_together = ('region', 'year', 'GHO', 'sex')

    def __str__(self):
        msg = f"""{self.sex} {self.GHO.lower()} for the
            {self.region} region for the year: {self.year}"""
        return msg
