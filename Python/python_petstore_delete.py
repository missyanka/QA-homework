import requests
import unittest

class TestStringMethods(unittest.TestCase):
	def test_delete_store(self):
		r = requests.delete('https://petstore.swagger.io/v2/store/order/10')
		print(r.status_code)
		assert r.status_code == 200
if __name__ == '__main__':
    unittest.main()