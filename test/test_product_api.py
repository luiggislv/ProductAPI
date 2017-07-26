import unittest
import requests
import json


class TestFlaskApiUsingRequests(unittest.TestCase):

    def test_create_product(self):
        url = "http://localhost:3000/product/new_product"
        product = {
            'name': 'Asus K555L',
            'description': 'Laptop Asus Model K555L',
            'category': 'Technology',
            'price': '$1200'
        }
        headers = { 'content-type': "application/json" }
        response = requests.request("POST", url, data=json.dumps(product), headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_list_product(self):
        response = requests.get('http://localhost:3000/product/list_product')
        self.assertEqual(response.status_code, 200)

    def test_list_product_id(self):
        response = requests.get('http://localhost:3000/product/list_product/1')
        self.assertEqual(response.status_code, 200)

    def test_update_product(self):
        url = "http://localhost:3000/product/update/1"
        product = {
            'name': 'Laptop Asus K555L',
            'description': 'Laptop Asus Model K555L',
            'category': 'Computers&Laptops',
            'price': '$1500'
        }
        headers = { 'content-type': "application/json" }
        response = requests.request("PUT", url, data=json.dumps(product), headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_delete_product(self):
        response = requests.delete('http://localhost:3000/product/delete/7')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
