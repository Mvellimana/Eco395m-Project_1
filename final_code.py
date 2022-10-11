import requests
import os
import csv
import operator


url = "https://api.yelp.com/v3/businesses/search"
key_j = "6aUvbW8QhdZuH7-1OIiSkm2Nu61twU2pwatNs0FxoT90NZ1iecSKsUGVZNg_GJyduGumAPlOlMG51r89ck1c3QH_E7i45ZUqhU2JWIadgCAzkpm3Fh19gLT48h5CY3Yx"
key_r = "Sol4vIOXEW3F6vyEqyOOK9GvZXRj0uNAMwuBVQXMp7zFLJ-XJGXAs8vMcTh0oCjai0qqfAdis6WzkqfQr9RXDrq3PvNwGvS4T7RSbVLWxcmYzTqa9GR7OXt_xv5CY3Yx"
key_t = "kejzjnuQGK-TuKjP3VRv0lh0BYNYwRwlnz35udZ2b8W5XyrU5vC6VZoHIaq_vdfux9AihTr3SpshUvAgIBR_ziReKf9zJQ8NiEWf_9wcCjAHdiEoe6ukWpIzWrxBY3Yx"




def data_from_specific_key(key):    
    restaurant_data = []
    headers = {
    "Authorization" : "Bearer %s" % key}
    for offset in range(0,1000,50):
        parameters = {
            "location" : "Austin TX",
            "limit" : 50,
            "term" : "restaurant",
            "offset" : offset
        }


        request = requests.get(url, headers = headers, params = parameters)
        if request.status_code == 200:
            for business in request.json()["businesses"]:
                individual = []
                id = business["id"]
                rating = business["rating"]
                is_closed = business["is_closed"]
                categories = business["categories"][0]["title"]
                name = business["name"]
                review_count = business["review_count"]
                coordinates = business["coordinates"]
                transactions = business["transactions"]
                address = business["location"]["display_address"]
                individual.append(id)
                individual.append(name)
                individual.append(is_closed)
                individual.append(rating)
                individual.append(review_count)
                individual.append(categories)
                individual.append(address)
                individual.append(coordinates)
                individual.append(transactions)
                
                if "price" in request.json()["businesses"][0].keys():
                    price = request.json()["businesses"][0]["price"]
                else:
                    price = " "
                individual.append(price)
                restaurant_data.append(individual)
        else:
            break

    return restaurant_data

keys = [key_j, key_r, key_t, key_j, key_r, key_t]
restaurants = []

for key in keys:
    restaurant_data = data_from_specific_key(key)
    for i in range(len(restaurant_data)):
        info = {
            "id": restaurant_data[i][0],
            "name": restaurant_data[i][1],
            "is closed": restaurant_data[i][2],
            "rating": restaurant_data[i][3],
            "review count": restaurant_data[i][4],
            "categories": restaurant_data[i][5],
            "address": restaurant_data[i][6],
            "coordinates": restaurant_data[i][7],
            "transaction types": restaurant_data[i][8],
            "price level": restaurant_data[i][9]
        }
        if info in restaurants:
            continue
        else:
            restaurants.append(info)



restaurants_sorted = sorted(restaurants, key = operator.itemgetter("id"), reverse=True)

with open("combined_results.csv", "w", encoding = "utf-8", newline="") as output_file:
    dict_writer = csv.DictWriter(output_file, fieldnames=["id", "name", "is closed", "rating", "review count", "categories", "address", "coordinates", "transaction types", "price level"])
    dict_writer.writeheader()
    dict_writer.writerows(restaurants_sorted)