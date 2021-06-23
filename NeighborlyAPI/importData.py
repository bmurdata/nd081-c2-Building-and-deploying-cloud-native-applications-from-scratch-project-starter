import azure.functions as func
import pymongo
import json 
url = "url"
client = pymongo.MongoClient(url)
database = client['db']
collection = database['advertisements']

collec2=database['posts']

with open('../sample_data/sampleAds.json') as file:
    file_data = json.load(file)
with open('../sample_data/samplePosts.json') as file:
    fd2 = json.load(file)

collection.insert_many(file_data)
collec2.insert_many(fd2)