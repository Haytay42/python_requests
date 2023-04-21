import pytest
from request_methods import *
import json

with open('pets_success.json') as f:
    pets = json.load(f)

with open('pets_incorrect.json') as f:
    pets_incorrect = json.load(f)


# Создание новых питомцев, статус код 200
@pytest.mark.parametrize('pet', pets)
def test_create_pet_success_code(pet):
    response = test_create_pet(pet)
    assert response.status_code == 200


# Создание новых питомцев, совпадают данные с json
@pytest.mark.parametrize('pet', pets)
def test_create_pet_success_data(pet):
    response = test_create_pet(pet)
    pet_data = response.json()
    assert pet_data == pet


#Создание новых питомцев с некорректными данными в параметре id
@pytest.mark.parametrize('pet_incorrect', pets_incorrect)
def test_create_pet_invalid_id(pet_incorrect):
    response = test_create_pet(pet_incorrect)
    assert response.status_code == 500