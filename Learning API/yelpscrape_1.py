from re import X
import requests as r
import pandas as pd
from itertools import product
import csv
from bs4 import BeautifulSoup
import operator
import os
import json

url = "https://api.yelp.com/v3/businesses/search"
key = "Sol4vIOXEW3F6vyEqyOOK9GvZXRj0uNAMwuBVQXMp7zFLJ-XJGXAs8vMcTh0oCjai0qqfAdis6WzkqfQr9RXDrq3PvNwGvS4T7RSbVLWxcmYzTqa9GR7OXt_xv5CY3Yx"
headers = {
    'Authorization': 'Bearer %s' % key,
}

url_params = {"location" : "Austin, TX",
                "limit" : 50,
                "term" : "restaurants",
                "offset" : 0,
                "locale" : "en_US"}

response = r.request('GET', url, headers=headers, params=url_params)
    
print(response.status_code)

restaurants_list = []
                       
request = r.get(url, headers = headers, params = url_params)
for business in response.json()["businesses"]:
    id = business["id"]
    name = business["name"]
    rating = business["rating"]
    #price = business["price"]
    restaurants_list.append([id,name,rating])
    
    
    restaurants = []
    
    for i in range(len(restaurants_list)):
        info = {
        "id": restaurants_list[i][0],
        "name": restaurants_list[i][1],
        "rating": restaurants_list[i][2]
        }

        restaurants.append(info)
    
#print(len(restaurants))
restaurants_sorted = sorted(restaurants, key = operator.itemgetter("id"), reverse=True)

with open("results.csv", "w", encoding = "utf-8", newline="") as output_file:
    dict_writer = csv.DictWriter(output_file, fieldnames=["id", "name", "rating"])
    dict_writer.writeheader()
    dict_writer.writerows(restaurants_sorted)

