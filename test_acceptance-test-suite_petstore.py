import variables
import petstore_requests
import json
import pytest

@pytest.fixture
def pet_id():
    pet_id = variables.generatePetID()
    return pet_id
@pytest.fixture
def pet_name():
    pet_name = variables.petName
    return pet_name

# TC0: Solution to the Test given. This test scenario
def test_CRUD_Pet(pet_id, pet_name):
    # Create and return a new Pet
    pet = petstore_requests.create_pet(pet_id, pet_name)
    assert pet.status_code == 200
    pet = json.loads(pet.content)

    # Verify The Pet was created with correct data
    petstore_requests.validate_response(pet)
    assert pet["name"] == pet_name
    assert pet["id"] == pet_id

    # Update this Pet_name, Verify update and return record
    updated_pet = petstore_requests.update_pet(pet_id, "Jack")
    assert updated_pet.status_code == 200
    updated_pet = json.loads(updated_pet.content)
    petstore_requests.validate_response(updated_pet)
    assert updated_pet["name"] == "Jack"
    assert updated_pet["id"] == pet_id

    # Delete the pet and demonstrate pet now deleted
    deleted_pet = petstore_requests.delete_pet(pet_id)
    assert deleted_pet.status_code == 200
    ghost_pet = petstore_requests.get_pet(pet_id)
    # Should retrun HTTP code 404 Not Found
    assert ghost_pet.status_code == 404


# TC1 : Create Pet and verify the response
def test_create_pet_verify_response(pet_id, pet_name):
    response = petstore_requests.create_pet(pet_id, pet_name)
    assert response.status_code == 200
    response_json = json.loads(response.content)
    request_json = petstore_requests.create_req_body(pet_id, pet_name)
    # verify the response content/values
    assert response_json == request_json
    # verify response data types
    petstore_requests.validate_response(json.loads(response.content))


# TC2: Update a pet name and verify the change
def test_update_pet_name_and_verify(pet_id, pet_name):
    new_name = "mark jones"
    response = petstore_requests.create_pet(pet_id, pet_name)
    assert response.status_code == 200
    updated_response = petstore_requests.create_pet(pet_id, new_name)
    assert updated_response.status_code == 200
    petstore_requests.validate_response(json.loads(response.content))
#   verifying updated name
    updated_response = json.loads(updated_response.content)
    assert updated_response["name"] == new_name


# TC3: Delete a pet and verify if the pet is deleted
def test_delete_pet_and_verify(pet_id, pet_name):
    response_newpet = petstore_requests.create_pet(pet_id, pet_name)
    response_get_newpet = petstore_requests.get_pet(pet_id)
    assert response_get_newpet.status_code == 200
    assert response_newpet.content == response_get_newpet.content
    # delete the new pet
    delete_response = petstore_requests.delete_pet(pet_id)
    assert delete_response.status_code == 200
    verification_response = petstore_requests.get_pet(pet_id)
    assert verification_response.status_code == 404

# The API host / API application allow to update a non existing user (like create/POST API)
# Hence checking the status code 200
# NOTE : The API we are accessing is Public API, hence there will be slight possibility of existing user with the same ID, I added static pet ID in next tests.
# as of now there are no user with that ID


def test_update_non_existing_pet(pet_name):
    response = petstore_requests.update_pet(45646545, pet_name)
    assert response.status_code == 200
    petstore_requests.delete_pet(45646545)


def test_delete_non_existing_pet():
    response = petstore_requests.delete_pet(65456446)
    assert response.status_code == 404


