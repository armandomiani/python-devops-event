import logging
import pprint


logging.basicConfig(level=logging.DEBUG)

# DEBUG - all content
# INFO - successful operations
# WARNING - failed operations, system working
# ERROR - feature not working, system working
# CRITICAL - system might not be working

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('/log.txt')
logger.addHandler(fh)


def calc(x, y):
    return x * y


obj = {
    'name': 'Armando',
    'city': {
        'name': 'Krakow',
        'state': {
            'name': 'Malopolska',
            'country': {
                'name': 'Poland'
            }
        }
    }
}

logger.info('Calc of {} and {} = {}'.format(10, 20, calc(10, 20)))
logger.debug(pprint.pformat(obj, indent=2))