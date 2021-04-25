#!/usr/bin/env python
from log import debug, info, warning, error, critical
import requests
import os

from pymongo import MongoClient

class ZunkaInterface():
    def __init__(self, run_mode='dev'):
        self.MONGO_CONN_STR = os.environ['MONGODB_HOST']
        #  if run_mode.lower().startswith('prod'):
        #  elif run_mode.lower().startswith('dev'):
        #  else:

    def get_all_products(self):
        with MongoClient(MONGO_CONN_STR) as client:
            print(client.list_database_names())
            db = client['zunka']
            print(db.list_collection_names())
            db_products = db['products']
            for product in db_products.find():
                print(product['storeProductTitle'])

    def get_all_products_with_meli_id(self):
        with MongoClient(self.MONGO_CONN_STR) as client:
            #  print(client.list_database_names())
            db = client['zunka']
            #  print(db.list_collection_names())
            db_products = db['products']
            #  for product in db_products.find({ 'mercadoLivreId': { '$exists': True } }, {'storeProductTitle': 1}):

            #  for product in db_products.find({ 'mercadoLivreId': { '$exists': True } }, {'storeProductTitle': 1}):
                #  print(product)

            return db_products.find({ 'mercadoLivreId': { '$exists': True } }, {'storeProductTitle': 1})

    def get_one_product(self):
        with MongoClient(self.MONGO_CONN_STR) as client:
            db = client['zunka']
            debug(db.list_collection_names())
            db_products = db['products']
            product = db_products.find_one()
            debug(product['storeProductTitle'])

#  print(get_all_meli_products())
#  get_all_products_with_meli_id()
