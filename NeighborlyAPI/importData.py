import azure.functions as func
import pymongo
import json 
url = "mongodb://neighborbm:5rgMDHvu7SCScgZvgFVQyxkSdavoFw09OGBb1E5FHSEvE0Xtt1rMEdh9epPslKQ8G1oEBZVl6vszyT1OC1uzOQ==@neighborbm.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborbm@"  # TODO: Update with appropriate MongoDB connection information
client = pymongo.MongoClient(url)
database = client['bneighborly']
collection = database['advertisements']

collec2=database['posts']

with open('../sample_data/sampleAds.json') as file:
    file_data = json.load(file)
with open('../sample_data/samplePosts.json') as file:
    fd2 = json.load(file)

collection.insert_many(file_data)
collec2.insert_many(fd2)