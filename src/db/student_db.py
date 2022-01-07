from db.database import Database

class StudentDB:
    def __init__(self,  cluster: str, collection: str):
        self.db = Database(cluster, collection)
        self.executeQuery = self.db.executeQuery
        self.executeAggregate = self.db.executeAggregate

    def create(self, character : dict):
        return self.db.collection.insert_one(character)

    def read(self):
        return self.executeQuery()
        

    def update(self, condition: dict, action: dict):
        return self.db.collection.update_one(condition, action)
    
    def delete(self, condition: dict):
        return self.db.collection.delete_one(condition)
    
    

