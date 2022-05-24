#!/usr/bin/env python
from logger import debug, info, warning, error, critical
import requests
import os
import json
import copy
from bson import ObjectId, json_util

from pymongo import MongoClient 

import util
import meli


class ZunkaInterface():
    def __init__(self, run_mode='dev'):
        self.MONGO_CONN_STR = os.environ['MONGODB_HOST']
        debug(f'Using db: {util.obfuscate_mongo_string_connection(self.MONGO_CONN_STR)}')
        #  print('__init__')
        #  print(self.MONGO_CONN_STR)
        #  if run_mode.lower().startswith('prod'):
        #  elif run_mode.lower().startswith('dev'):
        #  else:

    # test 
    def get_all_products_test(self):
        with MongoClient(self.MONGO_CONN_STR) as client:
            print(client.list_database_names())
            db = client['zunka']
            print(db.list_collection_names())
            db_products = db['products']
            for product in db_products.find():
                print(product['storeProductTitle'])

    # Return a dict (_id, product) for each product with a mercadoLivreId.
    def get_some_products(self, qtd=10):
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
            for product in col_products.find({ 'deletedAt': { '$exists': False } }).limit(qtd):
                #  print(product)
                products_by_id[str(product['_id'])] = product

            return products_by_id

    # Return a dict (_id, product) for each product with a mercadoLivreId.
    def get_all_products(self):
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
            for product in col_products.find({ 'deletedAt': { '$exists': False } }):
                #  print(product)
                products_by_id[str(product['_id'])] = product

            return products_by_id

    # Return a dict (_id, product) for each product with a mercadoLivreId.
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
            #  for product in col_products.find({ 'mercadoLivreId': { '$exists': True }, 'deletedAt': { '$exists': False } }):
            for product in col_products.find({ 'mercadoLivreId': { '$exists': True, '$ne': '' }, 'deletedAt': { '$exists': False } }):
                #  print(product)
                products_by_id[str(product['_id'])] = product

            return products_by_id

    # test
    def get_one_product(self):
        with MongoClient(self.MONGO_CONN_STR) as client:
            db = client['zunka']
            debug(db.list_collection_names())
            db_products = db['products']
            product = db_products.find_one()
            debug(product['storeProductTitle'])

    # Check zunka products consistence.
    def check_zunka_products_consistence(self, zunka_products, meli_products):
        debug('*** Checking Zunka products consistence ***')
        # For tests.
        result = {
            'no_meli_product': [],
            'no_back_reference': [],
            'not_equal': [],
            'updated': [],
        }
        # From zunka product list.
        for zunka_id, zunka_product in zunka_products.items():
            #  print(zunka_id)
            meli_id = zunka_product.get('mercadoLivreId')

            # No meli id.
            if meli_id == '' or meli_id == None:
                continue

            # No meli product.
            meli_product = meli_products.get(meli_id)
            if meli_product == None:
                warning(f'zunka product {zunka_id} with mercadoLivreId {meli_id} not found meli product')
                result['no_meli_product'].append(zunka_id)
                continue

            # No back reference.
            seller_custom_field = meli_product.get('seller_custom_field')
            if seller_custom_field != zunka_id:
                warning(f'zunka product {zunka_id} find meli product {meli_id} with seller_custom_field {seller_custom_field}, expect to be {zunka_id}')
                result['no_back_reference'].append(zunka_id)
                continue

            # Not equal.
            if not ZunkaInterface.is_zunka_product_and_meli_products_equal(zunka_product, meli_product):
                result['not_equal'].append(zunka_id)

        return result

    # Check meli products consistence.
    def check_meli_products_consistence(self, meli_products, zunka_products):
        debug('*** Checking Meli products consistence ***')
        # For tests.
        result = {
            'no_zunka_product': [],
            'no_back_reference': [],
            'not_equal': [],
            'updated': [],
        }

        # From meli product list.
        for meli_id, meli_product in meli_products.items():
            # No meli product associtade with zunka prodcut.
            zunka_id = meli_product.get('seller_custom_field')
            if zunka_id == '' or zunka_id == None:
                continue

            # No zunka product for meli product.
            zunka_product = zunka_products.get(zunka_id)
            if zunka_product == None:
                warning(f'Meli {meli_id} have no associated zunka product {zunka_id}')
                result['no_zunka_product'].append(zunka_id)
                continue

            # No back reference.
            mercadolivre_id = zunka_product.get('mercadoLivreId')
            if mercadolivre_id != meli_id:
                warning(f'Meli product {meli_id} find zunka product {zunka_id} with mercadoLivreId {mercadolivre_id}, expect to be {meli_id}')
                result['no_back_reference'].append(zunka_id)
                continue

            # Not equal.
            if not ZunkaInterface.is_zunka_product_and_meli_products_equal(zunka_product, meli_product):
                result['not_equal'].append(zunka_id)

        return result

    @staticmethod
    def is_zunka_product_and_meli_products_equal(zunka_product, meli_product):
        equal = True
        # Title.
        if zunka_product.get('storeProductTitle') != meli_product.get('title'):
            debug(
                f'zunka product {zunka_product.get("_id")} have different title from meli product {meli_product.get("id")}\n'
                f'\tzunka title: {zunka_product.get("storeProductTitle")}\n'
                f'\t meli title: {meli_product.get("title")}'
            )
            equal = False
        # Price.
        if (zunka_product.get('storeProductPrice') * 100 - meli_product.get('price')) > 1:
            debug(
                f'zunka product {zunka_product.get("_id")} have different price from meli product {meli_product.get("id")}\n'
                f'\tzunka price: {zunka_product.get("storeProductPrice")}\n'
                f'\t meli price: {meli_product.get("price")}'
            )
            equal = False
        # Meli stock must be up to max zunka stock. If meli have stock less than zunka, but at least one if have stock at zunka, its ok.
        # Stock 0 at zunka, meli must be 0.
        if (zunka_product.get('storeProductQtd') <= 0) and (meli_product.get('available_quantity') > 0):
            debug(
                f'zunka product {zunka_product.get("_id")} have 0 stock quantity and meli product {meli_product.get("id")} have stock\n'
                f'\tzunka available_quantity: {zunka_product.get("storeProductQtd")}\n'
                f'\t meli available_quantity: {meli_product.get("available_quantity")}'
            )
            equal = False
        # Zunka stock more than 0.
        else:
            # Meli have stock 0.
            if meli_product.get('available_quantity') <= 0:
                debug(
                    f'meli product {meli_product.get("id")} have stock 0, but zunka product {zunka_product.get("_id")} have stock > 0\n'
                    f'\tzunka available_quantity: {zunka_product.get("storeProductQtd")}\n'
                    f'\t meli available_quantity: {meli_product.get("available_quantity")}'
                )
                equal = False
            # Meli have stock bigger than zunka.
            if meli_product.get('available_quantity') > zunka_product.get('storeProductQtd'):
                debug(
                    f'meli product {meli_product.get("id")} have stock bigger than zunka product {zunka_product.get("_id")}\n'
                    f'\tzunka available_quantity: {zunka_product.get("storeProductQtd")}\n'
                    f'\t meli available_quantity: {meli_product.get("available_quantity")}'
                )
                equal = False

        return equal

    @staticmethod
    def update_zunka_product(self, zunka_product, meli_product):
        debug(f'todo - update zunka product {zunka_product["_id"]} from meli product {meli_product["id"]}')
        # If updated.
        return True

    # Return products from two list of products ids.
    @staticmethod
    def products_from_products_ids(products_ids_a, products_ids_b, products):
        # All zunka ids to update.
        all_products_ids = copy.copy(products_ids_a)
        for product_id in products_ids_b:
            if product_id not in all_products_ids:
                all_products_ids.append(product_id)

        # All zunka products to update.
        products_result = []
        for product_id in all_products_ids:
            products_result.append(products.get(product_id))

        return products_result


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

