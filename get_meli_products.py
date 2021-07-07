#!/usr/bin/env python

import requests
import os

import util
from zunka import ZunkaInterface
from meli import MeliInterface

# set run mode
run_mode = util.get_run_mode()
PROD, TEST, DEV = run_mode['PROD'], run_mode['TEST'], run_mode['DEV']
#  print(f'PROD: {PROD}, TEST: {TEST}, DEV: {DEV}')

#  zunka = ZunkaInterface()
#  zunka_products = zunka.get_all_products_with_meli_id()
#  print(list(zunka_products))
#  for key, value in zunka_products.items():
    #  print(key)
    #  print(value['storeProductTitle'])


meli = MeliInterface()
print(meli.get_all_products_id())

#  meli_products = meli.get_all_products()

#  print(f'type of: {type(meli_products)}')
#  key = next(iter(meli_products))
#  print(f' First item: {meli_products[key]["id"]}')
#  print(f' First item: {meli_products[key]["title"]}')
#  print(f' First item: {meli_products[key].get("title")}')

#  for key, value in meli_products.items():
    #  #  print(key)
    #  #  print(value)
    #  #  print(value.get('title'))
    #  print(f"[{value.get('seller_custom_field')}] - {key} - {value.get('title')}")

