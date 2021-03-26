
import pymongo

class Database(object):
    # URI = "mongodb+srv://admin:G1nestera@cluster0.a9jhp.mongodb.net/test"
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = 'goodteachingmusic'

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = 'goodteachingmusic'

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def find_all(collection):
        return Database.DATABASE[collection].find()