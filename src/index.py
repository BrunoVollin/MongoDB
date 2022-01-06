from db.characters_db import CharactersDB
from helpers.write_a_json import writeAJson


characters = CharactersDB(cluster="Aula", collection="Characters")

# # create
# characters.create({
#     "name": "Lightning McQueen",
#     "Films": [
#         "Cars",
#         "Cars 2",
#         "Cars 3"
#     ],
#     "Occupation": "race car"
# })

# read
data = characters.read()
writeAJson(data=data, name="test")

# update
characters.update(
    condition={"name": "Lightning McQueen", },
    action={"$set": {
        "Occupation": "Piston Cup Racer (in Cars and in Cars 3), World Grand Prix racer (in Cars 2), Mater's best friend and Cruz Ramirez's crew chief (in Cars 3)"}}
)

# # delete
# characters.delete({
#     "name": "Lightning McQueen"
# })
