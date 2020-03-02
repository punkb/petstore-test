import random
petID = random.randint(1, 100)
HOST_URL="https://petstore.swagger.io/v2/pet/"

requestHeaders={
    'api-key':'special-key',
    'Content-Type':'application/json'
    }
petName="mario"

body = {
        "id": petID,
        "category": {
            "id": petID+1,
            "name": "string"
        },
        "name": petName,
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "MAM"
            }
        ],
        "status": "available"
    }