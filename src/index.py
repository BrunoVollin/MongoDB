from db.student_db import StudentDB
from collections import OrderedDict
from validation.json_schema import validation


student = StudentDB(cluster="Schema", collection="schema")


student.create({
    "nome": "Rairon G. Ferreira",
            "ano": 2018,
            "curso": "GEC",
            "crs": 0.0,
            "endereço": {
                "cidade": "Itaúna, MG",
                "bairro": "Cerqueira Lima"
            }
})
