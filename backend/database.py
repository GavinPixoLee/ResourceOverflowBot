import os
import pymongo

client = pymongo.MongoClient(os.environ['DB_URI'])
database = client["ResourceOverflow"]

