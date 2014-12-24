from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
from urlparse import urljoin

class Ghost(object):
    # Only the ghost-admin client id is accepted
    client_id = 'ghost-admin'

    def __init__(self, base_url, username, password):
        self.base_url = base_url

        client = LegacyApplicationClient(self.client_id)
        self.ghost = OAuth2Session(self.client_id, client=client)

        # Fetch the access token
        self.ghost.fetch_token(
            self.url('ghost/api/v0.1/authentication/token'),
            username=username, password=password,
            body='client_id=%s' % self.client_id) # client_id must be included

    def url(self, relative):
        """Build full URL from relative path"""
        return urljoin(self.base_url, relative)

    def me(self):
        """Get info about me"""
        return self.ghost.get(self.url('ghost/api/v0.1/users/me/')).text
