#!/usr/bin/env python
from meli import MeliInterface
import json

class TestMeliAuth:
    def test_auth_envs(self):
        # development mode
        meli = str(MeliInterface())
        meli_user = meli.split(':')[0]
        meli_pass = meli.split(':')[1].split('@')[0]
        meli_host = meli.split('@')[1]
        assert meli_user[:3] == 'zun'
        assert meli_pass[:3] == 'sit'
        assert meli_host[:4] == 'http'

        # production mode
        meli = str(MeliInterface('prod'))
        meli_user = meli.split(':')[0]
        meli_pass = meli.split(':')[1].split('@')[0]
        meli_host = meli.split('@')[1]
        assert meli_user[:3] == 'zun'
        assert meli_pass[:3] == 'sit'
        assert meli_host[:4] == 'http'

    def test_get_token_access(self):
        meli = MeliInterface()
        token = meli.get_token_access()
        assert len(token) >= 10

class TestMeliProduct:
    def test_get_all_products_id(self):
        meli = MeliInterface()
        products = meli.get_all_products_id()
        assert len(products) > 0
        #  print(products)

    def test_get_products_from_ids(self):
        meli = MeliInterface()
        products_id = meli.get_all_products_id()[:4]
        products = meli.get_products_from_ids(products_id)
        assert len(products_id) == len(products)
        
    def test_get_all_products(self):
        meli = MeliInterface()
        products = meli.get_all_products()
        assert len(products) > 0
        # first key
        key = next(iter(products))
        assert key.startswith('MLB')
        assert products[key]['id'].startswith('MLB')

    def test_get_product(self):
        meli = MeliInterface()
        products = meli.get_all_products_id()
        assert len(products) > 0
        meli_product_id = products[0]
        print(f'Meli product to be get: {meli_product_id}')
        meli_product = meli.get_product(meli_product_id)
        print(f'id: {meli_product["id"]}')
        print(f'title: {meli_product["title"]}')
        print(f'available_quantity: {meli_product["available_quantity"]}')
        print(f'base_price: {meli_product["base_price"]}')
        print(f'price: {meli_product["price"]}')
        assert len(meli_product["title"]) > 0
        #  print(json.dumps(meli_product, indent=4, sort_keys=True))

    def test_update_product(self):
        meli = MeliInterface()
        products = meli.get_all_products_id()
        assert len(products) > 0
        meli_product_id = products[0]
        print(f'Meli product to be get: {meli_product_id}')
        meli_product = meli.get_product(meli_product_id)
        print(f'id: {meli_product["id"]}')
        print(f'title: {meli_product["title"]}')
        print(f'available_quantity: {meli_product["available_quantity"]}')
        print(f'base_price: {meli_product["base_price"]}')
        print(f'price: {meli_product["price"]}')
        assert len(meli_product["title"]) > 0
        #  print(json.dumps(meli_product, indent=4, sort_keys=True))

