import variables
import requests

url = variables.HOST_URL
headers = variables.requestHeaders
request_body = variables.body


def create_req_body(petID, petName):
    request_body["name"]=petName
    request_body["id"]=petID
    return request_body


def assertPetExist(petID):
    response = get_pet(petID)
    return (bool (response.status_code==200))


def create_pet(petID, petName):
    create_req_body(petID,petName)
    response = requests.post(url=url, headers=headers, json=request_body)
    return response


def get_pet(petID):
    response = requests.get(url=url + str(petID), headers=headers)
    return response


def update_pet(petID, name):
    request_body = create_req_body(petID, name)
    response = requests.put(url=url, headers=headers, json=request_body)
    return response


def delete_pet(petID):
    try:
        response = requests.delete(url=url + str(petID), headers=headers)
        return response
    except:
        print("Pet does not exist")


def validate_response(response):

    assert (type(response["id"])) == int
    assert (type(response["category"])) == dict
    assert (type(response["category"]["id"])) == int
    assert (type(response["category"]["name"])) == str
    assert (type(response["name"])) == str
    assert (type(response["photoUrls"])) == list
    for i in (response["photoUrls"]):
        assert (type(i)) == str
    assert (type(response["tags"])) == list
    assert (type(response["tags"][0])) == dict
    assert (type(response["tags"][0]["id"])) == int
    assert (type(response["tags"][0]["name"])) == str
    assert (type(response["status"])) == str










