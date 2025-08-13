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
      "adults":adults,
      "hl": "en",
      "api_key": "9d7d027cff59c9d81a06238f00abeb0574471f5da88e2ad8b7b5021c7002d8af"
    }

    return params

def searchdepartingflights(params):
  departflights = []
  search = GoogleSearch(params)
  results = search.get_dict()['best_flights']
  layoverqty = 0

  for item in results:
      flights = item.get('flights')
      layovers = item.get('layovers')
      if layovers != None:
         layoverqty = len(layovers)
         arrivalairport = flights[layoverqty]['arrival_airport']['name']
      else:
          arrivalairport = flights[0]['arrival_airport']['name']
          arrivaltime = flights[0]['arrival_airport']['time']
          layovers = 0
      departureairport = flights[0]['departure_airport']['name']
      departuretime = flights[0]['departure_airport']['time']
      arrivaltime = flights[0]['arrival_airport']['time']
      airplane = flights[0]['airplane']
      airline = flights[0]['airline']
      flightnumber = flights[0]['flight_number']
      departure_token = item.get('departure_token')
      totalduration = item.get('total_duration')
      price = item.get('price')
      flight_info = {
        "departureairport_dep":departureairport,
        "departuretime_dep": departuretime,
        "arrivalairport_dep": arrivalairport,
        "arrivaltime_dep": arrivaltime,
        "airplane_dep": airplane,
        "airline_dep": airline,
        "flightnumber_dep": flightnumber,
        "totalduration_dep": totalduration,
        "layoverqty_dep": layoverqty,
        "layovers_dep": layovers,
        "departure_token": departure_token,
        "price": price
      }
      departflights.append(flight_info)
  
  return departflights

def searchreturningflights(params):
  returnflights = []
  search = GoogleSearch(params)
  results = search.get_dict()
  layoverqty = 0

  if "best_flights" in results:
      results = search.get_dict()['best_flights']
  else:
      results = search.get_dict()['other_flights']

  for item in results:
      flights = item.get('flights')
      layovers = item.get('layovers')
      if layovers != None:
         layoverqty = len(layovers)
         arrivalairport = flights[layoverqty]['arrival_airport']['name']
      else:
          arrivalairport = flights[0]['arrival_airport']['name']
          arrivaltime = flights[0]['arrival_airport']['time']
      departureairport = flights[0]['departure_airport']['name']
      departuretime = flights[0]['departure_airport']['time']
      arrivaltime = flights[0]['arrival_airport']['time']
      airplane = flights[0]['airplane']
      airline = flights[0]['airline']
      flightnumber = flights[0]['flight_number']
      totalduration = item.get('total_duration')
      price = item.get('price')
      flight_info = {
        "departureairport_ret":departureairport,
        "departuretime_ret": departuretime,
        "arrivalairport_ret": arrivalairport,
        "arrivaltime_ret": arrivaltime,
        "airplane_ret": airplane,
        "airline_ret": airline,
        "flightnumber_ret": flightnumber,
        "totalduration_ret": totalduration,
        "layoverqty_ret": layoverqty,
        "layovers_ret": layovers,
        "price": price
      }
      returnflights.append(flight_info)
  
  return returnflights

def searchflights(departure, arrival, outbound_date, return_date, adults):
  vuelos = []
  opciones= []
  params = setparameters(departure, arrival, outbound_date, return_date, adults)

  departflights = searchdepartingflights(params)

  for i in range(0, len(departflights)):
      print(i)
      params.update({"departure_token": departflights[i]["departure_token"]})
      returnflights = searchreturningflights(params)
      vuelos.append(departflights[i])
      vuelos.append(returnflights[0])

  return vuelos

