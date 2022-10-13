# Yelp API Scraping (id, name, rating, price level)

""" Import the following libraries. """

from re import X
import requests as r
import pandas as pd
from itertools import product
import csv
from bs4 import BeautifulSoup
import operator
import os
import json

""" Credentials required. """
url = "https://api.yelp.com/v3/businesses/search"
key = "Sol4vIOXEW3F6vyEqyOOK9GvZXRj0uNAMwuBVQXMp7zFLJ-XJGXAs8vMcTh0oCjai0qqfAdis6WzkqfQr9RXDrq3PvNwGvS4T7RSbVLWxcmYzTqa9GR7OXt_xv5CY3Yx"
headers = {
    'Authorization': 'Bearer %s' % key,
}

"""Create a list to hold all the restaurants we scrape. """
restaurants_list = []

""" Scrape 1000 restaurants in Austin, Texas from Yelp. """
for offset in range(0,1000,50):
    url_params = {"location" : "Austin, TX",
                "limit" : 50,
                "term" : "restaurants",
                "offset" : offset,
                "locale" : "en_US"}

    response = r.request('GET', url, headers=headers, params=url_params)
    
    request = r.get(url, headers = headers, params = url_params)
    for business in response.json()["businesses"]:
        individual = []
        id = business["id"]
        name = business["name"]
        rating = business["rating"]
        
        if "price" in request.json()["businesses"][0].keys():
                    price = request.json()["businesses"][0]["price"]
                   
        else:
            price = " "
       
        individual.append(id)
        individual.append(name)
        individual.append(rating)
        individual.append(price)
        restaurants_list.append(individual)
  
""" Create a new list to hold the parameters scraped. """
restaurants = []

""" Scrape the parameters id, name, rating and price level from Yelp. """
for i in range(len(restaurants_list)):
    info = {
        "id": restaurants_list[i][0],
        "name": restaurants_list[i][1],
        "rating": restaurants_list[i][2],
        "price level": restaurants_list[i][3]
        }

    restaurants.append(info)
 
    """Takes the list (restaurants) and returns it post sorting in descending order. """   
sort_rest = sorted(restaurants, key = operator.itemgetter("id"), reverse=True)

""" Writes the list to a CSV. """
with open("results.csv", "w", encoding = "utf-8", newline="") as output_file:
     dict_writer = csv.DictWriter(output_file, fieldnames=["id", "name", "rating", "price level"])
     dict_writer.writeheader()
     dict2 = dict_writer.writerows(sort_rest)
    
