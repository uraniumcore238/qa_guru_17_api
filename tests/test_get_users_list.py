from pytest_voluptuous import S
from schemas.users_schema import users_list
from utils.sessions import base_url


def test_get_users_list():

    response = base_url().get("/users?page=2")
    assert response.status_code == 200
    assert S(users_list) == response.json()
