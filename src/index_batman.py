from helpers.write_a_json import writeAJson
from db.batman_db import BatmanDB

batmandb = BatmanDB(cluster="batman", collection="batwidgets")
batmandb.db.resetData()


# ? O custo total de todos o bat widgets
response = batmandb.db.collection.aggregate([
    {"$match": {"price": {"$exists": True}}},
    {"$project": {
        "type": 1,
        "price": 1,
        "_id": 0,

    }},
    {"$group": {
        "_id":  "$type",
        "total_price": {"$sum": "$price"}
    }},
    {"$sort": {"total_price": -1}}
])

writeAJson(data=response, name="O custo total de todos o bat widgets")


# # ? Quais BatWidgets são mais caros que 200
response = batmandb.db.collection.aggregate([
    {"$match": {"price": {"$exists": True}}},
    {"$project": {
        "_id": 0,
        "name": 1,
        "price": 1,
        "gte200": {
            "$cond": {
                "if": {"$gte": ["$price", 200]}, "then": 1, "else": 0
            }
        }
    }
    }
])

writeAJson(data=response, name="Mais caros que 200")
