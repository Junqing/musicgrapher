import requests
import hashlib
import time
import urllib
import json

api_profile = {
    "autocomplete": {
        "key": "y7bmngeyxr4as3xgqhzcuv9c",
        "shared_secret": "jGgJZTSUjT",
        "per_second_limit": 10,
        "per_day_limit": None
    },
    "metadata_search": {
        "key": "jtskvfmndszdurpt49z8mdv8",
        "shared_secret": "fNtXParHDs",
        "per_second_limit": 5,
        "per_day_limit": 3500
    },
    "tv_listing": {
        "key": "kaf34hapysdt2j9xybv6fb2h",
        "shared_secret": None,
        "per_second_limit": 5,
        "per_day_limit": 1000
    }
 }

 
#-----------------------------------------------------------------
class AllMusicGuide(object):
    api_url = 'http://api.rovicorp.com/search/v2.1'

    key = api_profile['metadata_search']['key']
    secret = api_profile['metadata_search']['shared_secret']

    def _sig(self):
        timestamp = int(time.time())

        m = hashlib.md5()
        m.update(self.key.encode('utf-8'))
        m.update(self.secret.encode('utf-8'))
        m.update(str(timestamp).encode('utf-8'))

        return m.hexdigest()

    def get(self, params=None):
        """Take a dict of params, and return what we get from the api"""

        if not params:
            params = {}
        params = urllib.parse.urlencode(params)

        sig = self._sig()

        url = "%s/%s?apikey=%s&sig=%s&%s" % (self.api_url, 'music/search', self.key, sig, params)

        print(url)
        
        resp = requests.get(url)

        if resp.status_code != 200:
            # THROW APPROPRIATE ERROR
            pass

        return resp.content
#------------------------------------------------------------------------
