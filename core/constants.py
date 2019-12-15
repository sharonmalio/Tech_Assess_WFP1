import json

from django.conf import settings

WHO_REGIONS = [
    ('Global', 'Global'),
    ('Africa', 'Africa'),
    ('Americas', 'Americas'),
    ('South-East Asia', 'South-East Asia'),
    ('Europe', 'Europe'),
    ('Eastern Mediterranean', 'Eastern Mediterranean'),
    ('Western Pacific', 'Western Pacific')
]

SEXES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Both sexes', 'Both sexes')
]

data_file = open(settings.DATA_FILE, 'r')
# reads the json file
DEFAULT_DATA = json.loads(data_file.read())
