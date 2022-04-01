#!/usr/bin/env python
from logger import debug, info, warning, error, critical

import requests
import os
import copy

import util
import platform
from zunka import ZunkaInterface
from meli import MeliInterface

# Python version.
debug(f'Python version: {platform.python_version()}')

# set run mode.
run_mode = util.get_run_mode()
PROD, TEST, DEV = run_mode['PROD'], run_mode['TEST'], run_mode['DEV']

zunka = ZunkaInterface()
zunka_products = zunka.get_all_products()
#  print(list(zunka_products))

#  debug(f'Zunka products with meli id: {len(zunka_products)}')
debug(f'All Zunka products: {len(zunka_products)}')
#  for key, value in zunka_products.items():
    #  print(key)
    #  print(value['storeProductTitle'])
#  print('\n')


#  debug('Temporary finish.')
#  exit()
#  print('Not exited!')


meli = MeliInterface()
meli_products = meli.get_active_products()
meli_products = MeliInterface.make_dic_id_product(meli_products)

debug(f'All Meli products: {len(meli_products)}')
#  for key, value in meli_products.items():
    #  print(key)
    #  print(value)

#  debug('Temporary finish.')
#  exit()
#  print('Not exited!')

# Check zunka products consistence.
check_result_zunka = zunka.check_zunka_products_consistence(zunka_products, meli_products)
debug(f'Zunka consitence result: {check_result_zunka}')

# Check meli products consistence.
check_result_meli = zunka.check_meli_products_consistence(meli_products, zunka_products)
debug(f'Meli consistence result: {check_result_meli}')

# All products to update.
zunka_products_to_update = zunka.products_from_products_ids(check_result_zunka.get('not_equal'), check_result_meli.get('not_equal'), zunka_products)
debug(f'Products to update: {zunka_products_to_update}')

# Update meli products.
for zunka_product in zunka_products_to_update:
    debug(f'Updating meli product {zunka_product["mercadoLivreId"]}, price: {zunka_product["storeProductPrice"]}, Quantity: {zunka_product["storeProductQtd"]}')
    #  meli.update_product(zunka_product['mercadoLivreId'], zunka_product['storeProductPrice'], zunka_product['storeProductQtd'])

debug('Finshed.')
