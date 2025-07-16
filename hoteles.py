from serpapi import GoogleSearch
import json

def setparameters(location, checkin, checkout, numberpeople):
    params = {
        "engine": "google_hotels",
        "q": location + "+hotels",
        "check_in_date": checkin,
        "check_out_date": checkout,
        "adults": numberpeople,
        "currency": "MXN",
        "gl": "us",
        "hl": "en",
        "api_key": "9d7d027cff59c9d81a06238f00abeb0574471f5da88e2ad8b7b5021c7002d8af"
    }

    return params

def searchhotels(location, checkin, checkout, numberpeople):
    hoteles = []
    params = setparameters(location, checkin, checkout, numberpeople)
    search = GoogleSearch(params)
    results = search.get_dict()['ads']

    for item in results:
       name = item.get('name')
       coordinates = item.get('gps_coordinates')
       rating = item.get('overall_rating')
       price = item.get('extracted_price')
       hotel_info = {
            "hotelname":name,
            "coordinates": coordinates,
            "rating": rating,
            "price": price
        }
       hoteles.append(hotel_info)

    return hoteles

#results = searchhotels("Chihuahua", "2025-08-15","2025-08-18", 2)

# params = setparameters("Chihuahua", "2025-08-15","2025-08-18", 2)
# search = GoogleSearch(params)
# results = search.get_dict()['ads']

# with open("outputhoteles.json", "w") as file:
#   json.dump(results, file, indent=4)# Code to write JSON data will go here

#print(results)

