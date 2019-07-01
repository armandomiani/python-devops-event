from sdk.api_resource import APIResource


class UserService(APIResource):
    resource = '/users'

    def list_all(self):
        super().fetch_get_request(self.resource)

    def create(self, user):
        super().fetch_post_request(self.resource, user)

    def update(self, user_id, user):
        url = '{}/{}'.format(self.resource, user_id)
        super().fetch_put_request(url, user)