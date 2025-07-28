from serpapi import GoogleSearch
import json

def setparameters(departure, arrival, outbound_date, return_date, adults):
    params = {
      "engine": "google_flights",
      "departure_id": departure,
      "arrival_id": arrival,
      "outbound_date": outbound_date,
      "return_date": return_date,
      "currency": "MXN",
      "adults": adults,
      "hl": "en",
      "api_key": "9d7d027cff59c9d81a06238f00abeb0574471f5da88e2ad8b7b5021c7002d8af"
    }

    return params

def searchflights(departure, arrival, outbound_date, return_date, adults):
  vuelos = []
  params = setparameters(departure, arrival, outbound_date, return_date, adults)
  search = GoogleSearch(params)
  results = search.get_dict()['best_flights']

  for item in results:
      flights = item.get('flights')
      layovers = item.get('layovers')
      if layovers != None:
         layoverqty = len(layovers)
         arrivalairport = flights[layoverqty]['arrival_airport']['name']
         arrivaltime = flights[layoverqty]['arrival_airport']['time']
      else:
          arrivalairport = flights[0]['arrival_airport']['name']
          arrivaltime = flights[0]['arrival_airport']['time']
      departureairport = flights[0]['departure_airport']['name']
      departuretime = flights[0]['departure_airport']['time']
      airplane = flights[0]['airplane']
      airline = flights[0]['airline']
      flightnumber = flights[0]['flight_number']
      totalduration = item.get('total_duration')
      price = item.get('price')
      flight_info = {
        "departureairport":departureairport,
        "departuretime": departuretime,
        "arrivalairport": arrivalairport,
        "arrivaltime": arrivaltime,
        "airplane": airplane,
        "airline": airline,
        "flightnumber": flightnumber,
        "totalduration": totalduration,
        "layoverqty": layoverqty,
        "layovers": layovers,
        "price": price
      }
      vuelos.append(flight_info)
  
  return vuelos
#with open("output.json", "w") as file:
#  json.dump(results, file, indent=4)# Code to write JSON data will go here
#Falta poder agregar las escalas que tienen ciertos vuelos, actualmente solo funciona bien para vuelos directos (15 julio 2025)