ENVS = {
    'dev': 'http://localhost:8080',
    'prod': 'http://api.something.com'
}


class APIResource(object):
    host_url = ''

    def __init__(self, environment='dev'):
        print('Running on {} env'.format(environment))
        self.host_url = ENVS[environment]

    def __build_endpoint(self, url):
        return '{}{}'.format(self.host_url, url)

    def __fetch_request(self, url, method='GET', post_data=None):
        url = self.__build_endpoint(url)
        print('Fetching a {} request to: {}'.format(method, url))
        
    def fetch_get_request(self, url):
        self.__fetch_request(url, 'GET')

    def fetch_post_request(self, url, post_data):
        self.__fetch_request(url, 'POST', post_data)
        print('Resource created using data:')
        print(post_data)

    def fetch_put_request(self, url, post_data):
        self.__fetch_request(url, 'PUT', post_data)
        print('Resource modified using data:')
        print(post_data)
