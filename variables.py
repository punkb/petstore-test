import random


def generatePetID():
    generatedpetID = random.randint(1, 10000)
    return generatedpetID


petID = random.randint(1, 100)


HOST_URL = "https://petstore.swagger.io/v2/pet/"

requestHeaders = {
    'api-key': 'special-key',
    'Content-Type': 'application/json'
    }


petName = "mario"


body = {
        "id": petID,
        "category": {
            "id": petID+1,
            "name": "string"
        },
        "name": petName,
        "photoUrls": [
            "www.example.com/photo"
        ],
        "tags": [
            {
                "id": petID+2,
                "name": "MAM"
            }
        ],
        "status": "available"
    }
