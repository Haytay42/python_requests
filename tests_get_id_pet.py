import pytest
from request_methods import *


# Проверка, что при существующем idPet приходит код 200
def test_get_request_status_code_success():
    response_code = test_get_request_status_code("https://petstore.swagger.io/v2/pet/10")
    assert response_code == 200

# Проверка корректных данных по существующему питомцу
def test_get_request_existing_pet():
    response = requests.get("https://petstore.swagger.io/v2/pet/10")
    assert response.json()["id"] == 10 and response.json()["name"] == "doggie"


# Проверка, что при несуществующих idPet приходит статус код 404
@pytest.mark.parametrize("idPet", [0, -1, 'test', ''])
def test_get_request_status_code_invalid(idPet):
    test_get_request_status_code(f"https://petstore.swagger.io/v2/pet/{idPet}")


# Проверка, что при несуществующих idPet приходит текст Pet not found
@pytest.mark.parametrize("idPet", [0, -1])
def test_get_request_pet_not_found(idPet):
    assert "Pet not found" in test_get_request_text(f"https://petstore.swagger.io/v2/pet/{idPet}")


# Проверка, что при некорректном формате idPet приходит текст unknown
@pytest.mark.parametrize("idPet", ['', 'test', 1.5])
def test_get_request_invalid_id(idPet):
    assert "unknown" in test_get_request_text(f"https://petstore.swagger.io/v2/pet/{idPet}")
