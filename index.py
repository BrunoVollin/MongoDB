from db.omnitrix_db import OmnitrixDB
from helpers.write_a_json import writeAJson

omni = OmnitrixDB(cluster="db_ben11", collection="aliens")

omni.getByName(name="Four Arms")
omni.getAll()
omni.getByPowerGT(power=2)
omni.getByBody(body="Humanoid")
omni.getByAbilities(abilities=["Tentacles", "Enhanced Durability"])

# power = 0 or velocity > 8
query = omni.executeQuery(
    project={
        "_id": 0,
        "name": 1,
        "numbers.power": 1,
        "numbers.velocity": 1
    }, 
    filter={
        "$or" : [
            {"numbers.power": {"$eq": 10}}, 
            {"numbers.velocity": {"$gt": 8}}
        ]
    }
)
writeAJson(data=query, name="power $eq 0 or velocity $gt 8")

# strength >= 5 nor intelligence < 10
query = omni.executeQuery(
    project={
        "_id": 0,
        "name": 1,
        "numbers.power": 1,
        "numbers.velocity": 1
    }, 
    filter={
        "$nor" : [
            {"numbers.strength": {"$gte": 5}}, 
            {"numbers.intelligence": {"$lt": 10}}
        ]
    }
)

writeAJson(data=query, name="strength $gte 5 nor intelligence $lt 10")
