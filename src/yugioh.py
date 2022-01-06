from helpers.write_a_json import writeAJson
from data.batman_database import dataset
import random



def convStrToIntAtJson(param: str):
        for i in dataset:
            if param in i:
                if i[param] != '?':
                    valueStr = i[param]
                    valueNum = int(valueStr)
                    i[param] = valueNum

def setRandomNumber(param: str):
        for i in dataset:
            if param in i:
                if i[param] != '?':
                    i[param] = random.randint(1000,2000)

setRandomNumber(param="custo")


writeAJson(data=dataset, name="sss")


