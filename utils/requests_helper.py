import logging
import curlify as curlify
from requests import Session
import allure


class BaseSession(Session):

    def __init__(self, **kwargs):
        self.base_url = kwargs.pop('base_url')
        super().__init__()

    def request(self, method, url, **kwargs):
        with allure.step(f'{method} {url}'):
            response = super().request(method, url=f'{self.base_url}{url}', **kwargs)
            msg = curlify.to_curl(response.request)
            logging.info(f'{response.status_code} {msg}')
            allure.attach(
                body=msg.encode('utf8'),
                name=f'Request {method} status code - {response.status_code}',
                attachment_type=allure.attachment_type.TEXT,
                extension='txt'
            )
        return response
