import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:hackdavis2020@majors-eo5my.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
