#!/usr/bin/env python
from logger import debug, info, warning, error, critical
import requests
from requests.auth import HTTPBasicAuth
import urllib.parse
import os

MELI_API_URL = 'https://api.mercadolibre.com'

USER_ID = os.environ['MERCADO_LIVRE_USER_ID']

class MeliInterface():
    def __init__(self, run_mode='dev'):
        if run_mode.lower().startswith('prod'):
            self.ZUNKASITE_HOST = os.environ['ZUNKASITE_HOST_PROD']
            self.ZUNKASITE_USER = os.environ['ZUNKASITE_USER_PROD']
            self.ZUNKASITE_PASS = os.environ['ZUNKASITE_PASS_PROD']
        else:
            self.ZUNKASITE_HOST = os.environ['ZUNKASITE_HOST_DEV']
            self.ZUNKASITE_USER = os.environ['ZUNKASITE_USER_DEV']
            self.ZUNKASITE_PASS = os.environ['ZUNKASITE_PASS_DEV']

    def get_token_access(self):
        headers = {}
        url = urllib.parse.urljoin(self.ZUNKASITE_HOST, 'meli/access-token')
        auth = HTTPBasicAuth(self.ZUNKASITE_USER, self.ZUNKASITE_PASS)
        r = requests.get(url, headers = headers, auth = auth)
        if r.status_code == requests.codes.ok:
            return r.text
        else:
            print('Fail to import token access.', r.status_code, r.text)

    def get_all_products_id(self):
        token_access = self.get_token_access()
        url = f'{MELI_API_URL}/users/{USER_ID}/items/search'
        headers = {'Authorization': f'Bearer {token_access}'}
        r = requests.get(url, headers=headers)
        #  print(f'get_all_products_id: {r.json()}')
        return r.json()['results']

    def get_active_products_id(self):
        token_access = self.get_token_access()
        #  url = f'{MELI_API_URL}/sites/MLB/search?seller_id={USER_ID}'
        url = f'{MELI_API_URL}/sites/MLB/search?seller_id={USER_ID}&attributes=results'
        r = requests.get(url)
        #  print(f'get_all_products_id: {r.json()}')
        return r.json()['results']

    # dict of producs by id from a list of meli products id
    def get_products_from_ids(self, meli_products_id):
        att = '&attributes={attributes,id,price,category_id,title,available_quantity,pictures,seller_custom_field,sold_quantity,status}'

        # create a list of products id, with max 10 by item list
        products_lists = MeliInterface.items_by_lists(meli_products_id)

        # create urls
        urls = []
        for item in products_lists:
            #  urls.append(f'{MELI_API_URL}/items?ids={",".join(item)}')
            urls.append(f'{MELI_API_URL}/items?ids={",".join(item)}/{att}')

        products = {}
        # request for each item list
        for url in urls:
            #  print(url)
            r = requests.get(url)
            # each product in the return list
            for product in r.json():
                if product['code'] == 200:
                    products[product['body']['id']] = product['body']
                else:
                    print(f'Error getting prodcut {product["body"]["id"]} from meli. Received code {product["code"]}')
        return products

    # get all products
    def get_all_products(self):
        return self.get_products_from_ids(self.get_all_products_id())

    # Get meli product.
    def get_product(self, meli_product_id):
        token_access = self.get_token_access()
        #  url = f'{MELI_API_URL}/users/{USER_ID}/items/search'
        url = f'{MELI_API_URL}/items/{meli_product_id}'
        headers = {'Authorization': f'Bearer {token_access}'}
        r = requests.get(url, headers=headers)
        #  print(f'get_product: {r.json()}')
        return r.json()

    # Update meli product price and quantity.
    def update_product(self, meli_product_id, price, quantity):
        token_access = self.get_token_access()
        #  url = f'{MELI_API_URL}/users/{USER_ID}/items/search'
        url = f'{MELI_API_URL}/items/{meli_product_id}'
        headers = {'Authorization': f'Bearer {token_access}'}
        json = {"price": price, "available_quantity": quantity}
        #  json = {"base_price": price, "available_quantity": quantity}
        print(f'json: {json}')
        r = requests.put(url, headers=headers, json=json)
        print(f'update_product_stock: {r.json()}')
        #  return r.json()['results']

    def log(self):
        debug(self.ZUNKASITE_HOST)

    @staticmethod
    def items_by_lists(items, max_size_list=10):
        l = []
        for i, v in enumerate(items):
            #  print(i, i//5, i%5, v)
            if (i % max_size_list) == 0:
                l.append([])
            l[i//max_size_list].append(v)
        return l

    def __repr__(self):
        return f'{self.ZUNKASITE_USER}:{self.ZUNKASITE_PASS}@{self.ZUNKASITE_HOST}'

    def __str__(self):
        return self.__repr__()

#  print(get_all_meli_products(
