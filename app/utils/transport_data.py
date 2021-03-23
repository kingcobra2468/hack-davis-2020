import requests
import json
import googlemaps
from datetime import datetime


class TransportData:

    def __init__(self, key, start, end):

        self.__key = key
        self.__start = start
        self.__end = end
        self.__gmaps = googlemaps.Client(key=key)
        self.__get_data(self.__start, self.__end)

    def __get_data(self, start, end):

        now = datetime.now()

        walk_result = self.__gmaps.directions(
            self.__start, self.__end, mode="walking", departure_time=now)
        cycle_result = self.__gmaps.directions(
            self.__start, self.__end, mode="bicycling", departure_time=now)
        transit_result = self.__gmaps.directions(
            self.__start, self.__end, mode="transit", departure_time=now)
        car_result = self.__gmaps.directions(
            self.__start, self.__end, mode="driving", departure_time=now)

        self.__transport_data_json = {
            'walk_result': walk_result,
            'cycling_result': cycle_result,
            'transit_result': transit_result,
            'car_result': car_result
        }

    def reload_data(self, start, end):
        self.__get_data(start, end)

    def get_transport_distances(self):

        walkString = self.__transport_data_json['walk_result'][0]["legs"][0]["distance"]["text"]
        cycleString = self.__transport_data_json['cycling_result'][0]["legs"][0]["distance"]["text"]
        transitString = self.__transport_data_json['transit_result'][0]["legs"][0]["distance"]["text"]
        carString = self.__transport_data_json['car_result'][0]["legs"][0]["distance"]["text"]

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
            "cycling": cycle_decimal,
            "transit": transit_decimal,
            "car": car_decimal,
        }
        return results

    def get_times(self):
        walkTimeString = self.__transport_data_json['walk_result'][0]["legs"][0]["duration"]["text"]
        cycleTimeString = self.__transport_data_json['cycling_result'][0]["legs"][0]["duration"]["text"]
        transitTimeString = self.__transport_data_json['transit_result'][0]["legs"][0]["duration"]["text"]
        carTimeString = self.__transport_data_json['car_result'][0]["legs"][0]["duration"]["text"]

        times = {
            "walk": walkTimeString,
            "cycling": cycleTimeString,
            "transit": transitTimeString,
            "car": carTimeString,
        }

        print(times)
        return times

    def get_co2(self):
        return dist_to_kWh(self.get_transport_distances())[1]

    def get_kwh(self):
        return dist_to_kWh(self.get_transport_distances())[0]


def dist_to_kWh(dict_co2):

    print(dict_co2)
    car_distance = dict_co2['car']
    transit_distance = dict_co2['transit']
    #train_distance = dict_co2['train']
    cycle_distance = dict_co2['cycling']
    walk_distance = dict_co2['walk']

    car_gallon = car_distance/24.9
    car_emission = car_distance*433.3408

    transit_gallon = transit_distance/9.1
    transit_emission = transit_distance*159.231

    cycle_calorie = 65.4*cycle_distance
    cycle_emission = 33.796*cycle_distance

    walk_calorie = 100*walk_distance
    walk_emission = 0

    car_energy = 36.6 * car_gallon
    transit_energy = 36.6 * transit_gallon
    cycle_energy = cycle_calorie
    walk_energy = walk_calorie

    dict_energy = {'car': car_energy, 'transit': transit_energy,
                   'cycle': int(cycle_energy), 'walk': int(walk_energy)}
    dict_emission = {'car': car_emission, 'transit': transit_emission,
                     'cycle': cycle_emission, 'walk': walk_emission}

    ret = [dict_energy, dict_emission]
    return ret
