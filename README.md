# petstore-test
This is rest API test CRUD using pet-store api.

# Prerequisites:
Python 3
python modules : `requests`, `pytest`, `json`, `jsonpath`, `unittest`

# How to Run 

1. Clone or download the repo.
2. Make sure you have the environment set up as given in prerequisite modules etc
3. Open the terminal (or the editor console) navigate to the  project directory 
4. run `pytest` command
5. it will run all the tests in petstore projects. 

# Project Structure
1. **petstore_requests.py** : Contains all the methods to access Pet store Rest API
2. **test_unnittest_petstore**: Contains all the unit tests
3. **test_acceptance-test-suite_petstore`**: Contains all the acceptance test
4. **variables.py** : Contains all the constants and input data for the tests. You can modify as you wish.

# Commands to run
To run all the tests use command `pytest`.
To run the scenario from the given Test. Please run the command : `pytest -k CRUD`. 
To run any specific test from use the name of the test in command : `pytest -k <name of the test>`
e.g `pytest -k update`.

