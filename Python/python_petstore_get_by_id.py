import requests
import unittest

class TestStringMethods(unittest.TestCase):
	def test_get_store(self):
		r = requests.get('https://petstore.swagger.io/v2/store/order/10')
		assert r.status_code == 200
if __name__ == '__main__':
    unittest.main()