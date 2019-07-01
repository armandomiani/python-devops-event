from http_helper import fetch_get_request
from sdk import client
import http_helper


def run_module():
    print('Exploring HttpHelper and FetchGetRequest function')
    print(dir(http_helper))
    code = http_helper.fetch_get_request.__code__
    help(http_helper.fetch_get_request)
    print(code.co_name)
    print(code.co_varnames)
    print('Running a script using http_helper module')
    fetch_get_request('api.allegro.pl')


def run_package():
    print('Getting the user list from API...')
    print(client.get_users())

if __name__ == '__main__':
    # run_module()
    run_package()
