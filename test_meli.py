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

    def test_get_active_products_id(self):
        meli = MeliInterface()
        products = meli.get_active_products_id()
        assert len(products) > 0
        print(json.dumps(products[0], indent=4, sort_keys=True))
        print(f'Products len: {len(products)}')

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
        print(f'Meli products cound: {len(products)}')

        not_paused_meli_product_found = False
        for meli_product_id in products:
            meli_product = meli.get_product(meli_product_id)
            if meli_product['status'] == 'paused':
                print(f'Product {meli_product["id"]} paused')
            else:
                not_paused_meli_product_found = True
                break

        print(f'not_paused_meli_product_found: {not_paused_meli_product_found}')
        print(f'meli_product found: {meli_product["id"]}')
        print(f'meli_product for: {meli_product_id}')
        exit

        print(f'Meli product to be get: {meli_product_id}')
        meli_product = meli.get_product(meli_product_id)
        #  print(json.dumps(meli_product, indent=4, sort_keys=True))
        product_id = meli_product["id"]
        product_qty = meli_product["available_quantity"]
        product_price = meli_product["base_price"]
        print(f'id: {product_id}')
        print(f'title: {meli_product["title"]}')
        print(f'available_quantity: {product_qty}')
        print(f'base_price: {meli_product["base_price"]}')
        print(f'price: {product_price}')
        assert product_qty > 0
        # Can do the test if product not have stock.
        assert meli_product["available_quantity"] > 0
        product_qty = product_qty - 1
        product_price = product_price + 1
        print(f'Quantity: {product_qty}, price: {product_price}')
        #  meli.update_product(product_id, product_price, product_qty)


        #  print(json.dumps(meli_product, indent=4, sort_keys=True))

