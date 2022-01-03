import pymongo
from db.omini_dataset import dataset

class Database:
    def __init__(self, cluster: str, collection: str):
        self.clusterConnection = pymongo.MongoClient(
            "mongodb+srv://adm:adm@cluster0.bqedr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
            tlsAllowInvalidCertificates=True
        )
        self.db = self.clusterConnection[cluster]
        self.collection = self.db[collection]
        

    def resetData(self):
        self.collection.drop()
        self.collection.insert_many(dataset)
