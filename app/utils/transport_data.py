import requests
import json
import googlemaps
from datetime import datetime

def get_transport_distances(start, end):

    gmaps = googlemaps.Client(key = 'AIzaSyCm5kzVdeaLePWkUoiPqrWGR3mmrmtGezg')
    now = datetime.now()
    
    walk_result = gmaps.directions(start, end, mode = "walking", departure_time = now)
    cycle_result = gmaps.directions(start, end, mode = "bicycling", departure_time = now)
    transit_result = gmaps.directions(start, end, mode = "transit", departure_time = now)
    car_result = gmaps.directions(start, end, mode = "driving", departure_time = now)

    walkString = walk_result[0]["legs"][0]["distance"]["text"]
    cycleString = cycle_result[0]["legs"][0]["distance"]["text"]
    transitString = transit_result[0]["legs"][0]["distance"]["text"]
    carString = car_result[0]["legs"][0]["distance"]["text"]

    walkString = walkString[0:-2]
    cycleString = cycleString[0:-2]
    transitString = transitString[0:-2]
    carString = carString[0:-2]
    
    walk_decimal = float(walkString.replace(",", ""))
    cycle_decimal = float(cycleString.replace(",", ""))
    transit_decimal = float(transitString.replace(",", ""))
    car_decimal = float(carString.replace(",", ""))

    results = {
        "walk": walk_decimal,
        "cycle": cycle_decimal,
        "transit": transit_decimal,
        "car": car_decimal,
    }

    return results

def dist_to_kWh(dict_co2):

    car_distance = dict_co2['car']
    transit_distance = dict_co2['transit']
    #train_distance = dict_co2['train']
    cycle_distance = dict_co2['cycle']
    walk_distance = dict_co2['walk']

    car_gallon = car_distance/24.9
    car_emission = car_distance*433.3408

    transit_gallon = transit_distance/9.1
    transit_emission = transit_distance*159.231

    #train_gallon = train_distance/470
    #train_emission = train_distance*159.231

    cycle_calorie = 65.4*cycle_distance
    cycle_emission = 33.796*cycle_distance

    walk_calorie = 100*walk_distance
    walk_emission = 0

    car_energy = 36.6* car_gallon
    transit_energy = 36.6 * transit_gallon
    cycle_energy = cycle_calorie/860420.65
    #train_energy = 36.6 * train_gallon
    walk_energy = walk_calorie/860420.65

    #dict_energy = {car_energy:'car',transit_energy:'transit',train_energy:'train',cycle_energy:'cycle',walk_energy:'walk'}
    #dict_emission = {car_emission: 'car', transit_emission: 'transit', train_emission: 'train', cycle_emission: 'cycle', walk_emission: 'walk'}

    dict_energy = {'car': car_energy, 'transit': transit_energy, 'cycle': cycle_energy,'walk': walk_energy}
    dict_emission = { 'car': car_emission, 'transit': transit_emission, 'cycle': cycle_emission, 'walk': walk_emission}

    ret = [dict_energy,dict_emission]
    return ret

#def get_energy_and_emissions(start,end):
#    return convert(distanceBetween(start,end))
