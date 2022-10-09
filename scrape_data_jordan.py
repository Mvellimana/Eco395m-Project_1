import requests


url = "https://api.yelp.com/v3/businesses/search"
key = "6aUvbW8QhdZuH7-1OIiSkm2Nu61twU2pwatNs0FxoT90NZ1iecSKsUGVZNg_GJyduGumAPlOlMG51r89ck1c3QH_E7i45ZUqhU2JWIadgCAzkpm3Fh19gLT48h5CY3Yx"
headers = {
    "Authorization" : "Bearer %s" % key
}

restaurant_data = []

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
            restaurant_data.append(individual)
    else:
        break




