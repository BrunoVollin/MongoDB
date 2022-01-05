import pymongo

class Database:
    def __init__(self, cluster: str, collection: str, dataset: dict):
        self.clusterConnection = pymongo.MongoClient(
            "mongodb+srv://adm:adm@cluster0.bqedr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
            tlsAllowInvalidCertificates=True
        )
        self.db = self.clusterConnection[cluster]
        self.collection = self.db[collection]
        self.dataset = dataset

    def executeQuery(self, project={}, filter={}):
        response = self.collection.find(filter, project)

        result = []
        for index in response:
            result.append(index)

        return result
        
    def resetData(self):
        self.collection.drop()
        self.collection.insert_many(self.dataset)
