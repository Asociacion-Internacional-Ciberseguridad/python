import requests
from requests_oauthlib import OAuth1

auth = OAuth1('TU_CONSUMER_KEY', 'TU_CONSUMER_SECRET', 'TU_ACCESS_TOKEN', 'TU_ACCESS_SECRET')

response = requests.get('https://api.twitter.com/1.1/account/verify_credentials.json', auth=auth)
print(response.json())
