from pymongo.mongo_client import MongoClient
import time

def mongoDB():    
    client = MongoClient()
    db = client.users
    col = db.portal_users
    result = db.portal_user.insert(
        {
            "username": "afunk",
            "ip_address": "192.168.56.5",
            "login_time": time.time()
        }
    )
    cursor = col.find({})
    for document in cursor:
        pprint(document)
    
mongoDB()
