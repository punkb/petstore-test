import unittest
import variables
import petstore_requests
import json

url = variables.HOST_URL
headers = variables.requestHeaders
petName = variables.petName
request_body = variables.body


class petstoreUnitTests(unittest.TestCase):

    def test_create_pet(self):
        pet_id = variables.generatePetID()
        pet_name = variables.petName
        response = petstore_requests.create_pet(pet_id, pet_name)
        petstore_requests.validate_response(json.loads(response.content))
        assert response.status_code == 200

    def test_get_pet(self):
        pet_id = variables.generatePetID()
        pet_name = variables.petName
        petstore_requests.create_pet(pet_id, pet_name)
        response = petstore_requests.get_pet(pet_id)
        assert response.status_code == 200

    def test_update_pet(self):
        pet_id = variables.generatePetID()
        pet_name = variables.petName
        response = petstore_requests.update_pet(pet_id, pet_name + " johnson ")
        assert response.status_code == 200

    def test_delete_pet(self):
        pet_id = variables.generatePetID()
        pet_name = variables.petName
        petstore_requests.create_pet(pet_id, pet_name)
        response = petstore_requests.delete_pet(pet_id)
        assert response.status_code == 200

    def test_assertPetExist(self):
        pet_id = variables.generatePetID()
        pet_name = variables.petName
        petstore_requests.create_pet(pet_id, pet_name)
        assert petstore_requests.assertPetExist(pet_id) == True

    def test_create_req_body(self):
        pet_id = variables.generatePetID()
        pet_name = variables.petName
        response = petstore_requests.create_pet(pet_id, pet_name)
        petstore_requests.validate_response(json.loads(response.content))





















