import requests



def test_get_request_status_code(url):
    try:
        response = requests.get(url)
        return response.status_code
    except Exception:
        raise ValueError("No status code")


def test_get_request_text(url):
    try:
        response = requests.get(url)
        return response.text
    except Exception:
        raise ValueError("No text")


def test_create_pet(pets):
    try:
        return requests.post('https://petstore.swagger.io/v2/pet', json=pets)
    except Exception:
        raise ValueError("Error while creating a pet")


def test_delete_pet(pets):
    try:
        return requests.delete(f'https://petstore.swagger.io/v2/pet/{pets["id"]}')
    except Exception:
        raise ValueError("Error while deleting a pet")


