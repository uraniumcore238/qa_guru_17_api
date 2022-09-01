import pytest
from schemas.single_user_schema import single_user
from utils.sessions import base_url
from pytest_voluptuous import S


@pytest.mark.parametrize('user_id', [2, 3, 4])
def test_get_single_user(user_id):
    user = user_id
    response = base_url().get(f"/users/{user}")
    assert response.status_code == 200
    assert S(single_user) == response.json()


