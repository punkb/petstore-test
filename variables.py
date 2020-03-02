import random


def generatePetID():
    generatedpetID = random.randint(1, 10000)
    return generatedpetID


HOST_URL = "https://petstore.swagger.io/v2/pet/"

requestHeaders = {
    'api-key': 'special-key',
    'Content-Type': 'application/json'
    }


petName = "Mario"


body = {
        "id": generatePetID(),
        "category": {
            "id": generatePetID()+1,
            "name": "string"
        },
        "name": petName,
        "photoUrls": [
            "www.example.com/photo"
        ],
        "tags": [
            {
                "id": generatePetID()+2,
                "name": "MAM"
            }
        ],
        "status": "available"
    }
