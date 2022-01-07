import pymongo

class Database:
    def __init__(self, cluster: str, collection: str):
        self.clusterConnection = pymongo.MongoClient(
            "mongodb+srv://bruno:bruno@cluster0.b01wt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
            tlsAllowInvalidCertificates=True
        )
        self.db = self.clusterConnection[cluster]
        self.collection = self.db[collection]

    def executeQuery(self, project={"_id": 0}, filter={}):
        response = self.collection.find(filter, project)

        result = []
        for index in response:
            result.append(index)

        return result

    def executeAggregate(self, params: list):
        response = self.collection.aggregate(params)

        result = []
        for index in response:
            result.append(index)

        return result

        
    def resetData(self, dataset: dict):
        self.collection.drop()
        self.collection.insert_many(self.dataset)
