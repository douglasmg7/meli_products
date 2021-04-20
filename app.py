#!/usr/bin/env python

import requests
import os

import util
import zunka
#  import meli

# set run mode
run_mode = util.get_run_mode()
PROD, TEST, DEV = run_mode['PROD'], run_mode['TEST'], run_mode['DEV']
#  print(f'PROD: {PROD}, TEST: {TEST}, DEV: {DEV}')

#  zunka.set_production()
#  print(f'zunka mode: {zunka.get_run_mode()}')

zunka_products = zunka.get_all_products_with_meli_id()
print(list(zunka_products))
