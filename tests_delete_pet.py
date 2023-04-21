import pytest
from request_methods import *
import json

with open('pets_success.json') as f:
    pets = json.load(f)

with open('pets_incorrect.json') as f:
    pets_incorrect = json.load(f)


# Удаление существующих питомцев
@pytest.mark.parametrize('pet', pets)
def test_delete_pet_success_code(pet):
    response = test_delete_pet(pet)
    assert response.status_code == 200


# Удаление несуществующих питомцев
@pytest.mark.parametrize('pet')
def test_delete_pet_success_code(pet):
    response = test_delete_pet(pet)
    assert response.status_code == 404


# Удаление несуществующих питомцев
@pytest.mark.parametrize('pet', pets_incorrect)
def test_delete_pet_success_code(pet):
    response = test_delete_pet(pet)
    assert response.status_code == 404