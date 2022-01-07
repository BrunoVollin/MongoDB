validation = {"$jsonSchema":
{
        "bsonType": "object",
        "required": ["nome", "ano", "curso", "endereço"],
        "properties": {
            "nome": {
                "bsonType": "string",
                "description": "deve ser uma string e é obrigatória"
            },
            "ano": {
                "bsonType": "int",
                "minimum": 1965, 
                "maximum": 2022,
                "description": "deve ser um inteiro entre [1965, 2021] e é obrigatório"
            },
            "curso": {
                "enum": ["GEC", "GEB", "GEA", "GEE", "GET", "GEP", "GES"],
                "description": "deve ser um dos valores de 'enum' e é obrigatório"
            },
            "crs": {
                "bsonType": ["double"], # podemos adicionar o tipo "int" aqui
                "description": "deve ser um double se o campo existir"
            },
            "endereço": {
                "bsonType": "object",
                "required": ["cidade"],
                "properties": {
                    "bairro": {
                        "bsonType": "string",
                        "description": "deve ser uma string se o campo existir"
                    },
                    "cidade": {
                        "bsonType": "string",
                        "description": "deve ser uma string e é obrigatório"
                    }
                }
            }
        }
    }
}