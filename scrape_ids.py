import requests


url = "https://api.yelp.com/v3/businesses/search"
key = "6aUvbW8QhdZuH7-1OIiSkm2Nu61twU2pwatNs0FxoT90NZ1iecSKsUGVZNg_GJyduGumAPlOlMG51r89ck1c3QH_E7i45ZUqhU2JWIadgCAzkpm3Fh19gLT48h5CY3Yx"
headers = {
    "Authorization" : "Bearer %s" % key
}

restaurant_ids = []

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
            id = business["id"]
            restaurant_ids.append(id)
    else:
        break

print(restaurant_ids)