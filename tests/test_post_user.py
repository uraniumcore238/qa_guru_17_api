from schemas.new_user_schema import new_user
from utils.sessions import base_url
from pytest_voluptuous import S


parameters = {
    "name": "Test Name",
    "job": "QA Engineer"
}


def test_post_user():

    response = base_url().post('/users', json=parameters)
    assert response.status_code == 201
    dict_json_data = response.json()
    name = parameters['name']
    job = parameters['job']
    assert name == dict_json_data['name']
    assert job == dict_json_data['job']


def test_post_user_schema_validation():

    response = base_url().post('/users', json=parameters)
    assert response.status_code == 201
    assert S(new_user) == response.json()
