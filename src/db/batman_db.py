from helpers.write_a_json import writeAJson
from db.database import Database
from data.batman_dataset import dataset


class BatmanDB:
    def __init__(self,  cluster: str, collection: str):
        self.db = Database(cluster, collection, dataset)
        self.executeQuery = self.db.executeQuery
        self.executeAggregate = self.db.executeAggregate
    
    

