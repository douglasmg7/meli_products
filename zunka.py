#!/usr/bin/env python

import requests
import os

from pymongo import MongoClient

host = 'localhost'
port = '27017'
name = 'zunka'
user = 'app'
password = 'zunKa4a'

mongo_connection_string = f'mongodb://{user}:{password}@{host}:{port}/{name}?authSource=admin';

#  print(mongo_connection_string)

def get_all_products():
    with MongoClient(mongo_connection_string) as client:
        print(client.list_database_names())
        db = client['zunka']
        print(db.list_collection_names())
        db_products = db['products']
        for product in db_products.find():
            print(product['storeProductTitle'])

def get_all_products_with_meli_id():
    with MongoClient(mongo_connection_string) as client:
        #  print(client.list_database_names())
        db = client['zunka']
        #  print(db.list_collection_names())
        db_products = db['products']
        #  for product in db_products.find({ 'mercadoLivreId': { '$exists': True } }, {'storeProductTitle': 1}):
        for product in db_products.find({ 'mercadoLivreId': { '$exists': True } }, {'storeProductTitle': 1}):
            print(product)

def get_one_product():
    with MongoClient(mongo_connection_string) as client:
        print(client.list_database_names())
        db = client['zunka']
        print(db.list_collection_names())
        db_products = db['products']
        product = db_products.find_one()
        print(product['storeProductTitle'])

def get_all_meli_products():
    url = f'https://api.mercadolibre.com/users/{user_id}/items/search'
    headers = {'Authorization': f'Bearer {token_access}'}
    r = requests.get(url, headers=headers)
    return r.json()['results']

#  print(get_all_meli_products())
get_all_products_with_meli_id()
