from helpers.write_a_json import writeAJson
from db.database import Database
from data.ben10_dataset import dataset


class Ben10DB:
    def __init__(self,  cluster: str, collection: str):
        self.db = Database(cluster, collection, dataset)
        self.executeQuery = self.db.executeQuery
        
    def getAll(self):
        project = {"_id": 0}
        filter = {}

        response =self.executeQuery(filter=filter, project=project)
        writeAJson(data=response, name="getAll()")
        return response

    def getByName(self, name: str):
        project = {"_id": 0}
        filter = {"name": {"$eq" : name}}

        response = self.executeQuery(filter=filter, project=project)
        writeAJson(data=response, name=f"getByName( {name} )")
        return response

    def getByPowerGT(self, power: int):
        project = {
            "name": 1,
            "_id": 0,
            "numbers.power": 1
        }
        filter = {
            "numbers.power": {"$gt": power}
        }

        response = self.executeQuery(filter=filter, project=project)
        writeAJson(data=response, name=f"getByPowerGT( {power} )")
        return response

    def getByBody(self, body: str):
        project = {
            "name": 1,
            "_id": 0,
            "body": 1
        }
        filter = {
            "body": {"$regex" :  body}
        }

        response = self.executeQuery(filter=filter, project=project)
        writeAJson(data=response, name=f"getByBody( {body} )")
        return response

    def getByAbilities(self, abilities: list):
        project = {
            "name": 1,
            "_id": 0,
            "abilities": 1
        }
        filter = {
            "abilities": {"$in" :  abilities}
        }

        response = self.executeQuery(filter=filter, project=project)
        writeAJson(data=response, name=f"getByAbilities( {abilities} )")
        return response
