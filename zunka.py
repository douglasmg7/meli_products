#!/usr/bin/env python

import requests
import os

from pymongo import MongoClient

#  host = 'localhost'
#  port = '27017'
#  name = 'zunka'
#  user = 'app'
#  password = 'zunKa4a'

#  MONGO_CONN_STR = f'mongodb://{user}:{password}@{host}:{port}/{name}?authSource=admin'

PROD = False
DEV = True

MONGO_CONN_STR = os.environ['MONGODB_HOST']

def set_production():
    global PROD
    global DEV
    PROD = True
    DEV = not PROD

def get_run_mode():
    global PROD
    global DEV
    return { 'PROD': PROD, 'DEV': DEV }

def get_all_products():
    with MongoClient(MONGO_CONN_STR) as client:
        print(client.list_database_names())
        db = client['zunka']
        print(db.list_collection_names())
        db_products = db['products']
        for product in db_products.find():
            print(product['storeProductTitle'])

def get_all_products_with_meli_id():
    with MongoClient(MONGO_CONN_STR) as client:
        #  print(client.list_database_names())
        db = client['zunka']
        #  print(db.list_collection_names())
        db_products = db['products']
        #  for product in db_products.find({ 'mercadoLivreId': { '$exists': True } }, {'storeProductTitle': 1}):

        #  for product in db_products.find({ 'mercadoLivreId': { '$exists': True } }, {'storeProductTitle': 1}):
            #  print(product)

        return db_products.find({ 'mercadoLivreId': { '$exists': True } }, {'storeProductTitle': 1})


def get_one_product():
    with MongoClient(MONGO_CONN_STR) as client:
        print(client.list_database_names())
        db = client['zunka']
        print(db.list_collection_names())
        db_products = db['products']
        product = db_products.find_one()
        print(product['storeProductTitle'])

#  print(get_all_meli_products())
#  get_all_products_with_meli_id()
