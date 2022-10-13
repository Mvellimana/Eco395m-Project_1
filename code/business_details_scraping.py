import json

#Get id, coordinates, is_closed, location.display_address
def extract_id_from_business(data):
    business_id = data["id"]

    return business_id

def extract_is_closed_from_business(data):
    is_closed = data["is_closed"] 

    return is_closed

def extract_coordinates_from_business(data):
    business_coordinates = data["coordinates"]

    return business_coordinates

def extract_display_address_from_business(data):
    display_address = data["location"]["display_address"]

    return display_address

def extract_info_from_business(data):
    is_closed = extract_is_closed_from_business(data)
    business_id = extract_id_from_business(data)
    business_coordinates = extract_coordinates_from_business(data)
    display_address = extract_display_address_from_business(data)
    business = {
        "id": business_id,
        "is_closed": is_closed,
        "coordinates": business_coordinates,
        "display_address": display_address
    }

    return business

def extract_info_per_business(raw_business_data):
    data = json.loads(raw_business_data)
    info = extract_info_from_business(data)

    return info


#Expecteds
expected_id = "gR9DTbKCvezQlqvD7_FzPw"
expected_is_closed = False
expected_latitude = 37.787789124691 
expected_longitude = -122.399305736113
expected_display_address_line1 = "123 Second St"
expected_display_address_line2 = "San Francisco, CA 94105"
expected_business = {
    'id': expected_id,
    'is_closed': expected_is_closed,
    'coordinates': {'latitude': expected_latitude, 'longitude': expected_longitude},
    'display_address': [expected_display_address_line1, expected_display_address_line2]
    }


#Test data
test_business = """{
    "id": "gR9DTbKCvezQlqvD7_FzPw",
    "alias": "north-india-restaurant-san-francisco-7",
    "name": "North India Restaurant",
    "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/_nJ2VTeTZe5-gePr8PXTxg/o.jpg",
    "is_claimed": true,
    "is_closed": false,
    "url": "https://www.yelp.com/biz/north-india-restaurant-san-francisco-7?adjust_creative=oapS1_QZo4-Es35G1UKw_g&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_lookup&utm_source=oapS1_QZo4-Es35G1UKw_g",
    "phone": "+14153481234",
    "display_phone": "(415) 348-1234",
    "review_count": 2133,
    "categories": [
        {
            "alias": "indpak",
            "title": "Indian"
        },
        {
            "alias": "fooddeliveryservices",
            "title": "Food Delivery Services"
        },
        {
            "alias": "catering",
            "title": "Caterers"
        }
    ],
    "rating": 4.0,
    "location": {
        "address1": "123 Second St",
        "address2": "",
        "address3": "",
        "city": "San Francisco",
        "zip_code": "94105",
        "country": "US",
        "state": "CA",
        "display_address": [
            "123 Second St",
            "San Francisco, CA 94105"
        ],
        "cross_streets": ""
    },
    "coordinates": {
        "latitude": 37.787789124691,
        "longitude": -122.399305736113
    },
    "photos": [
        "https://s3-media1.fl.yelpcdn.com/bphoto/_nJ2VTeTZe5-gePr8PXTxg/o.jpg",
        "https://s3-media4.fl.yelpcdn.com/bphoto/W2oBBWPGm3bRYEuHKGMtCw/o.jpg",
        "https://s3-media1.fl.yelpcdn.com/bphoto/AHm5LPigScMuUG-bT9jqdw/o.jpg"
    ],
    "price": "$$",
    "hours": [
        {
            "open": [
                {
                    "is_overnight": false,
                    "start": "1000",
                    "end": "2300",
                    "day": 0
                },
                {
                    "is_overnight": false,
                    "start": "1000",
                    "end": "2300",
                    "day": 1
                },
                {
                    "is_overnight": false,
                    "start": "1000",
                    "end": "2300",
                    "day": 2
                },
                {
                    "is_overnight": false,
                    "start": "1000",
                    "end": "2300",
                    "day": 3
                },
                {
                    "is_overnight": false,
                    "start": "1000",
                    "end": "2330",
                    "day": 4
                },
                {
                    "is_overnight": false,
                    "start": "1000",
                    "end": "2330",
                    "day": 5
                },
                {
                    "is_overnight": false,
                    "start": "1000",
                    "end": "2300",
                    "day": 6
                }
            ],
            "hours_type": "REGULAR",
            "is_open_now": true
        }
    ],
    "transactions": [
        "pickup",
        "restaurant_reservation",
        "delivery"
    ]
}"""



# Results unit test

data = json.loads(test_business)

result = extract_id_from_business(data)
assert result == expected_id

result = extract_is_closed_from_business(data)
assert result == expected_is_closed

result = extract_coordinates_from_business(data)
assert result["latitude"] == expected_latitude
assert result["longitude"] == expected_longitude

result = extract_display_address_from_business(data)
assert result[0] == expected_display_address_line1
assert result[1] == expected_display_address_line2

result = extract_info_from_business(data)
assert result == expected_business