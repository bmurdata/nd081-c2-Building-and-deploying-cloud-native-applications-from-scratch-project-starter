import azure.functions as func
import pymongo
import dbsetup
def main(req: func.HttpRequest) -> func.HttpResponse:
    print("Trying to get a json of the data or something")
    request = req.get_json()

    if request:
        try:
            url = dbsetup.myurl
            client = pymongo.MongoClient(url)
            database = client[dbsetup.db]
            collection = database['advertisements']
            print(request)

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )