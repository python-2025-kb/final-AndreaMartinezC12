from serpapi import GoogleSearch
import json

def setparameters(location):
    params = {
        "engine": "google",
        "q": "Things+to+do+in+" + location,
        "api_key": "9d7d027cff59c9d81a06238f00abeb0574471f5da88e2ad8b7b5021c7002d8af"
    }

    return params

def search_attractions(location):
    sights = []
    params = setparameters(location)
    search = GoogleSearch(params)
    results = search.get_dict()
    top_sights = results["top_sights"]["sights"]
    with open("outputatracciones.json", "w") as file:
        json.dump(top_sights, file, indent=4)
    
    for item in top_sights:
      name = item['title']
      thumbnail = item['thumbnail']
      if "price" in item:
          sightprice = item['price']
      else:
            sightprice = "Free"
      sights_info = {
        "name": name,
        "thumbnail": thumbnail,
        "price": sightprice
      }
      sights.append(sights_info)

    return sights