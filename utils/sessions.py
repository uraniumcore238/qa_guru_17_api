import os
from utils.requests_helper import BaseSession


def base_url() -> BaseSession:
    root_url = os.getenv('reqres_url')
    return BaseSession(base_url=root_url)
