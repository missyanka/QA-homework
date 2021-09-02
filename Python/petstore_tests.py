import requests
import unittest
import time

class TestStringMethods(unittest.TestCase):
    ORDER_ID = "12312312312337"
    def test_1_get_stores(self):
        print("Test#1")
        response = requests.get("https://petstore.swagger.io/v2/store/inventory")
        assert response.status_code == 200, response.text

    def test_2_post_store(self):
        print("Test#2")
        url = "https://petstore.swagger.io/v2/store/order"
        params = {
            "id": self.ORDER_ID,
            "petId": 0,
            "quantity": 0,
            "status": "placed",
            "complete": True
        }
        response = requests.post(url, json=params)
        assert response.status_code == 200, response.text

    def test_3_get_store(self):
        print("Test#3")
        response = requests.get("https://petstore.swagger.io/v2/store/order/" + self.ORDER_ID)
        assert response.status_code == 200, response.text

    def test_4_delete_store(self):
        print("Test#4")
        response = requests.delete("https://petstore.swagger.io/v2/store/order/" + self.ORDER_ID)
        print(response.status_code)
        assert response.status_code == 200, response.text

if __name__ == "__main__":
    unittest.main()