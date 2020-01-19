import json

class BuildingDataController:

    def __init__(self, file):

        self.__file = file

    def get_data(self):

        data = None

        with open(self.__file, "r") as json_raw:
            data = json.load(json_raw)

        return data 