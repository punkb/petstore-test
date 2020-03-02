import variables
import petstore_requests
import json
import unittest

url=variables.HOST_URL
headers=variables.requestHeaders
petID=variables.petID
petName=variables.petName


# Test to create a pet
def test_create_pet():
    response = petstore_requests.create_pet(petID)
    assert response.status_code == 200


#Test to verify the created pet
def test_verify_created_pet():
    response = petstore_requests.create_pet(petID)
    response_json = json.loads(response.content)
    request_body = petstore_requests.create_req_body(petID,petName)
    assert response_json == request_body


# Test to fetch the created pet
def test_get_pet():
    response=petstore_requests.get_pet(petID)
    assert response.status_code==200


# Test to update the pet_name
def test_update_pet_name():
    response = petstore_requests.update_pet(petID, petName+"update")
    assert response.status_code==200


# Test to update and verify the updated pet
def test_update_and_verify_pet_name():
    response = petstore_requests.update_pet(petID, petName+"update1")
    response_json = json.loads(response.content)
    request_body = petstore_requests.create_req_body(petID, petName+"update1")
    assert response_json==request_body


# Test tp delete the pet
def test_delete_pet():
    response = petstore_requests.delete_pet(petID)
    assert response.status_code==200


# Negetive test
def test_delete_pet_negative():
    response = petstore_requests.delete_pet(petID)
    assert response.status_code == 404





