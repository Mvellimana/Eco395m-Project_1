import requests as r
import pandas as pd
from itertools import product

url = 'https://api.yelp.com/v3/businesses/search'
key = 'Sol4vIOXEW3F6vyEqyOOK9GvZXRj0uNAMwuBVQXMp7zFLJ-XJGXAs8vMcTh0oCjai0qqfAdis6WzkqfQr9RXDrq3PvNwGvS4T7RSbVLWxcmYzTqa9GR7OXt_xv5CY3Yx'
headers = {
    'Authorization': 'Bearer %s' % key,
}

url_params = {"location" : "Austin, TX",
                "limit" : 50,
                "term" : "restaurants",
                "offset" : 0,
                "locale" : "en_US"}

response = r.request('GET', url, headers=headers, params=url_params)
    
#print(response.json())

restaurants_list = []
                       
request = r.get(url, headers = headers, params = url_params)
for business in response.json()['businesses']:
  name = business["name"]
  rating = business["rating"]
  #price = business["price"]
  restaurants_list.append([name,rating])
