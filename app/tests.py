import unittest
import json
from flask import url_for
from server import app

class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()

    def test_main_page(self):
        response = self.client.get('/')
        self.assertTrue('Hello, World!' in response.get_data(as_text=True))

    def test_register_with_empty_params(self):
        response = self.client.post('/users/orgs/',
                        data=json.dumps({}))
        json_response = json.loads(response.data)
        self.assertTrue('message' in json_response)
        self.assertTrue(json_response['message'] == 'No parameters are specified.')

    def test_register_with_some_params(self):
        params = {'name': 'Mahidol'}
        response = self.client.post('/users/orgs/',
                    data=json.dumps(params),
                    content_type="application/json")
        json_response = json.loads(response.data)
        self.assertTrue('message' in json_response)
        self.assertTrue(json_response['message'] == 'success')


if __name__ == '__main__':
    unittest.main()