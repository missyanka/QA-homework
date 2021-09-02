import requests
import unittest

class TestStringMethods(unittest.TestCase):
	def test_onliner(self):
		r = requests.get('https://www.onliner.by/')
		assert r.status_code == 200
if __name__ == '__main__':
    unittest.main()