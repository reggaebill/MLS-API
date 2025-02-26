#####import requests
import json
from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
from Credentials import *

class Property():
    def __init__(self):
        self.street = ''
        self.city = ''
        self.state = ''
        self.clip = ''

    def get_clip(self, state, city, street):
        self.state = state
        self.city = city
        self.street = street
        property_s = oauth.get(
            f'https://property.corelogicapi.com/v2/properties/search?streetAddress={self.street}&city={self.city}&state={self.state}',
            headers=headers)
        property_json = json.loads(property_s.text)
        print(property_json)
        smaller_dict = property_json['items']
        self.clip = smaller_dict[0]['clip']
        #print(self.clip)
        #print(property_json)


    def property_scan(self):
        #oauth.get(f'https://property.corelogicapi.com/v2/properties/{clip}/property-detail', headers=headers)
        r = oauth.get(f'https://property.corelogicapi.com/v2/properties/{self.clip}/property-detail', headers=headers)
        #print(r)
        r_parsed = json.loads(r.text)
        print(r_parsed['buildings'])


oauth = OAuth2Session(client=LegacyApplicationClient(client_id=client_id))
token = oauth.fetch_token(token_url='https://api-prod.corelogic.com/oauth/token?grant_type=client_credentials',
        username=username, password=password, client_id=client_id,
        client_secret=client_secret)

headers = {'Authorization': 'Bearer {token}', 'Content-Type': 'application/json', 'x-developer-email': (username)}
property = 'https://property.corelogicapi.com/v2/properties/search'
clip = '1010258757'
#r = oauth.get(f'https://property.corelogicapi.com/v2/properties/{clip}/property-detail', headers=headers)
#print(r)
#r_parsed = r.json()
#print(r_parsed)

listing = Property()
listing.get_clip('FL', 'Tampa', '3213 E GENESEE Street')
#listing.property_scan()
