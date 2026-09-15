#!/usr/bin/env python

from fastapi import status
from fastapi.testclient import TestClient

# Import the app from
from .the_fast_api import theApp

client = TestClient(theApp)


# Test if we get good HTTP status (status 200) when we ask for the JSON
def test_getGoodStatus():
    response = client.get("/static-dict")
    assert response.status_code == status.HTTP_200_OK


# Test that all the keys are present in the returned dictionary.
def test_allKeysPresent():
    response = client.get("/static-dict")
    dictionary = response.json()
    keysToTest = [
        "firstName",
        "lastName",
        "numPets",
        "usesPiApproximation",
        "likesAurorasTooMuch",
    ]
    for keyToTest in keysToTest:
        assert keyToTest in dictionary


# Test that all the keys are of the correct type.
def test_keysCorrectType():
    response = client.get("/static-dict")
    dictionary = response.json()
    assert type(dictionary["firstName"]) is str
    assert type(dictionary["lastName"]) is str
    assert type(dictionary["numPets"]) is int
    assert type(dictionary["usesPiApproximation"]) is float
    assert type(dictionary["likesAurorasTooMuch"]) is bool


# Test the values returned (normally would not get down to this level)


# Test first name
def test_firstNameValue():
    response = client.get("/static-dict")
    dictionary = response.json()
    assert dictionary["firstName"] == "Niles"


# Test last name
def test_lastNameValue():
    response = client.get("/static-dict")
    dictionary = response.json()
    assert dictionary["lastName"] == "Oien"


# Test number of pets
def test_numPetsValue():
    response = client.get("/static-dict")
    dictionary = response.json()
    assert dictionary["numPets"] == 5


# Test usesPiApproximation
def test_usesPiApproximationValue():
    response = client.get("/static-dict")
    dictionary = response.json()
    assert dictionary["usesPiApproximation"] == 3.141


# Test likesAurorasTooMuch
def test_likesAurorasTooMuchValue():
    response = client.get("/static-dict")
    dictionary = response.json()
    desiredValue = True
    assert dictionary["likesAurorasTooMuch"] == desiredValue
