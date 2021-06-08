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

#  zunka.set_production()
#  print(f'zunka mode: {zunka.get_run_mode()}')

zunka = ZunkaInterface()
zunka_products = zunka.get_all_products_with_meli_id()
#  print(list(zunka_products))
#  for key, value in zunka_products.items():
    #  #  print(key)
    #  print(value['storeProductTitle'])


meli = MeliInterface()
meli_products = meli.get_all_products()
#  for key, value in meli_products.items():
    #  print(key)
    #  print(value)

# Check zunka products consistence.
zunka.check_zunka_meli_products_consistence(zunka_products, meli_products)

