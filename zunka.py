#!/usr/bin/env python
from logger import debug, info, warning, error, critical
import requests
import os
import json
from bson import ObjectId, json_util

from pymongo import MongoClient 

import meli


class ZunkaInterface():
    def __init__(self, run_mode='dev'):
        self.MONGO_CONN_STR = os.environ['MONGODB_HOST']
        #  print('__init__')
        #  print(self.MONGO_CONN_STR)
        #  if run_mode.lower().startswith('prod'):
        #  elif run_mode.lower().startswith('dev'):
        #  else:

    def get_all_products(self):
        with MongoClient(self.MONGO_CONN_STR) as client:
            print(client.list_database_names())
            db = client['zunka']
            print(db.list_collection_names())
            db_products = db['products']
            for product in db_products.find():
                print(product['storeProductTitle'])

    # return a dict with key _id for each product with a mercadoLivreId
    def get_all_products_with_meli_id(self):
        with MongoClient(self.MONGO_CONN_STR) as client:
            #  print(client.list_database_names())
            db_zunka = client['zunka']
            #  print(db_zunka.list_collection_names())
            col_products = db_zunka['products']
            #  for product in col_products.find({ 'mercadoLivreId': { '$exists': True } }, {'storeProductTitle': 1}):

            #  for product in col_products.find({ 'mercadoLivreId': { '$exists': True } }, {'storeProductTitle': 1}):
                #  print(product)

            #  return col_products.find({ 'mercadoLivreId': { '$exists': True } }, {'storeProductTitle': 1})
            #  return col_products.find({ 'mercadoLivreId': { '$exists': True } })

            products_by_id = {}
            for product in col_products.find({ 'mercadoLivreId': { '$exists': True } }):
                #  print(product)
                products_by_id[str(product['_id'])] = product

            return products_by_id

    def get_one_product(self):
        with MongoClient(self.MONGO_CONN_STR) as client:
            db = client['zunka']
            debug(db.list_collection_names())
            db_products = db['products']
            product = db_products.find_one()
            debug(product['storeProductTitle'])

    def check_zunka_meli_products_consistence(self, zunka_products, meli_products):
        for zunka_id, zunka_product in zunka_products.items():
            meli_id = zunka_product['mercadoLivreId']
            if meli_id == '' or meli_id == None:
                warning(f'Zunka product {zunka_id} not have mercadoLivreId')
                continue
            meli_product = meli_products.get(meli_id)
            if meli_product == None:
                warning(f'Not have meli product for zunka product {zunka_id} with mercadoLivreId {meli_id}')
                continue
            if meli_product['seller_custom_field'] != zunka_id:
                warning(f'Meli product {meli_id} have associated zunka product {meli_product["seller_custom_field"]}, expect to be {zunka_id}')
                continue
            if not is_zunka_product_and_meli_products_equal():
                update_meli_product()

    def is_zunka_product_and_meli_products_equal(self, zunka_product, meli_product):
        debug(f'todo - check {zunka_product["_id"]} is equal {meli_product["id"]}')
        return True

    def update_zunka_product(self, zunka_product, meli_product):
        debug(f'todo - update {zunka_product["_id"]} from {meli_product["id"]}')

    def update_meli_product(self, meli_product, zunka_product):
        debug(f'todo - update {meli_product["id"]} from {zunka_product["_id"]}')

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

def saveDic(dic, file_name):
    with open(file_name, 'w') as file:
        file.write(json_util.dumps(dic, indent=4, sort_keys=True))

def loadDic(file_name):
    with open(file_name) as file:
        return json_util.loads(file.read())

