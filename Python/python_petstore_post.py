import requests
import unittest

class TestStringMethods(unittest.TestCase):
    def test_post_store(self):
        url = 'https://petstore.swagger.io/v2/store/order'
        params = {
            "id": 10,
            "petId": 0,
            "quantity": 0,
            "shipDate": "2021-09-01T20:02:09.240Z",
            "status": "placed",
            "complete": True
        }
        r = requests.post(url, json=params)
        assert r.status_code == 200
if __name__ == '__main__':
    unittest.main()