import requests
import json
import googlemaps
from datetime import datetime

class TransportData:

    def __init__(self, key, start, end):
        
        #'AIzaSyCm5kzVdeaLePWkUoiPqrWGR3mmrmtGezg'
        self.__key = key
        self.__start = start
        self.__end = end
        self.__gmaps = googlemaps.Client(key = key)
        self.__get_data()

    def __get_data(self, start = self.__start, end = self.__end):

        now = datetime.now()

        walk_result = self.__gmaps.directions(self.__start, self.__end, mode = "walking", departure_time = now)
        cycle_result = self.__gmaps.directions(self.__start, self.__end, mode = "bicycling", departure_time = now)
        transit_result = self.__gmaps.directions(self.__start, self.__end, mode = "transit", departure_time = now)
        car_result = self.__gmaps.directions(self.__start, self.__end, mode = "driving", departure_time = now)

        self.__transport_data_json = {
            'walking_result' : walk_result,
            'cycle_result' : cycle_result,
            'transit_result' : transit_result,
            'car_result' : car_result
        }

def reload_data(self, start = self.__start, end = self.__end):
    self.__get_data(start, end)

def get_transport_distances(start, end):

    gmaps = googlemaps.Client(key = 'AIzaSyCm5kzVdeaLePWkUoiPqrWGR3mmrmtGezg')
    now = datetime.now()
    
    walk_result = gmaps.directions(start, end, mode = "walking", departure_time = now)
    cycle_result = gmaps.directions(start, end, mode = "bicycling", departure_time = now)
    transit_result = gmaps.directions(start, end, mode = "transit", departure_time = now)
    car_result = gmaps.directions(start, end, mode = "driving", departure_time = now)

    walkString = self.__transport_data_json['walking_result'][0]["legs"][0]["distance"]["text"]
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
def get_time():
    pass

def get_co2():
    pass

def get_kwh():
    pass

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
