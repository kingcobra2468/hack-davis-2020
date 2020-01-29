import googlemaps
from kwh_building_data_controller import BuildingDataController

def get_list_of_Locations():
    gmaps = googlemaps.Client(key='AIzaSyC-dtV6daEa4v20nabi4CJkKZX2FPPcTSk')

    # Geocoding an address
    dictData = BuildingDataController("/Users/rekhathomas/Desktop/AwarenessWebsite/app/models/kwh_building_data.json").get_data()
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
    locationList = []
    weightList = []

    for address in dictData.keys():
        print(address)
        geocode_result = gmaps.geocode(address)
        locationList.append(geocode_result[0]["geometry"]["location"])
        weightList.append(dictData[address])
        print(geocode_result[0]["geometry"]["location"])
    print(locationList)
    print(weightList)
    return locationList