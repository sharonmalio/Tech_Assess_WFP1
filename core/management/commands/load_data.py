"""Management command for loadind data"""

from django.core.management import BaseCommand

from core.constants import DEFAULT_DATA
from core.models import WHOLifeExpectancy


def load_data():
    """Function to help with handling data"""
    facts = DEFAULT_DATA['fact']
    for fact in facts:
        data = dict()
        data.update({
            'GHO': fact['dim']['GHO'],
            'region': fact['dim']['REGION'],
            'year': fact['dim']['YEAR'],
            'sex': fact['dim']['SEX'],
            'number_of_years': fact['Value']
        })
        WHOLifeExpectancy.objects.update_or_create(
            #allow not to load data twice
            #unpacking data
            **data
        )

#similiar setup with runserver
class Command(BaseCommand):
    help = 'Load data from constants file'
    #overwritting handle to allow
    def handle(self, *args, **options):
        try:
            load_data()
            self.stdout.write(self.style.SUCCESS('Data loaded sucessfully'))
        except Exception:
            self.stdout.write(self.style.ERROR('Error encountered while loading data'))
