import unittest
import requests
import json
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from product_api import db
from product_api.models import Product


class appTests(unittest.TestCase):

    def setUp(self):
        db.drop_all()
        db.create_all()
        product_test1 = Product(name="Asus_K557",description="Laptop Asus Model K557",category="Laptops",price="$1200")
        product_test2 = Product(name="Asus_K558",description="Laptop Asus Model K558",category="Laptops",price="$1250")
        db.session.add(product_test1)
        db.session.add(product_test2)
        db.session.commit()

    def test_create_product(self):
        url = "http://localhost:3000/product"
        product = {'name': 'Asus_K559', 'description': 'Laptop Asus Model K559', 'category': 'Technology', 'price': '$1200'}
        headers = { 'content-type': "application/json" }
        response = requests.request("POST", url, data=json.dumps(product), headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_list_product(self):
        response = requests.get('http://localhost:3000/product')
        self.assertEqual(response.status_code, 200)

    def test_list_product_filterByCategory(self):
        response = requests.get('http://localhost:3000/product?category=Laptops')
        self.assertEqual(response.status_code, 200)

    def test_get_product_byId(self):
        response = requests.get('http://localhost:3000/product/1')
        self.assertEqual(response.status_code, 200)

    def test_update_product_byId(self):
        url = "http://localhost:3000/product/1"
        product = {'name': 'Asus_K557', 'description': 'Laptop Asus Model K557', 'category': 'Laptops', 'price': '$1300'}
        headers = { 'content-type': "application/json" }
        response = requests.request("PUT", url, data=json.dumps(product), headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_delete_product_byId(self):
        response = requests.delete('http://localhost:3000/product/1')
        self.assertEqual(response.status_code, 200)

    def test_get_product_byName(self):
        response = requests.get('http://localhost:3000/product/Asus_K558')
        self.assertEqual(response.status_code, 200)

    def test_update_product_byName(self):
        url = "http://localhost:3000/product/Asus_K558"
        product = {'name': 'Asus_K558', 'description': 'Laptop Asus Model K558', 'category': 'Laptops', 'price': '$2800'}
        headers = { 'content-type': "application/json" }
        response = requests.request("PUT", url, data=json.dumps(product), headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_delete_product_byName(self):
        response = requests.delete('http://localhost:3000/product/Asus_K558')
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        db.drop_all()
        db.session.remove()

if __name__ == "__main__":
    unittest.main()
