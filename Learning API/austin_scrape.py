import requests
import numpy as np
import pandas as pd
from itertools import product
from business_details_scraping import extract_info_per_business

# Credentials: key, url, headers
search_url = "https://api.yelp.com/v3/businesses/search"
business_url = "https://api.yelp.com/v3/businesses/"
key = "kejzjnuQGK-TuKjP3VRv0lh0BYNYwRwlnz35udZ2b8W5XyrU5vC6VZoHIaq_vdfux9AihTr3SpshUvAgIBR_ziReKf9zJQ8NiEWf_9wcCjAHdiEoe6ukWpIzWrxBY3Yx"
headers = {
    "Authorization" : "Bearer %s" % key, 
    "Accept": "application/json"
}

# Scrape:
restaurant_ids = []

for offset in range(0,1000,50):
    parameters = {
        "location" : "Austin TX",
        "limit" : 50,
        "term" : "restaurant",
        "offset" : offset
    }


    result = requests.get(search_url, headers = headers, params = parameters)
    if result.status_code == 200:
        for business in result.json()["businesses"]:
            print(".")
            id = business["id"]
            restaurant_ids.append(id)
    else:
        print(result.status_code)
        print(result.reason)
        break


print(restaurant_ids)

for id in restaurant_ids:
    result = requests.get(business_url + id, headers = headers)
    if result.status_code == 200:
        print(".")
        business_info = extract_info_per_business(result.text)
        print(business_info)
        print("")
    else:
        print(result.status_code)
        print(result.reason)
        break
