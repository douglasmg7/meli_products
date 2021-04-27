#!/usr/bin/env python
from meli import MeliInterface

def test_auth_envs():
    # development mode
    meli = str(MeliInterface())
    meli_user = meli.split(':')[0]
    meli_pass = meli.split(':')[1].split('@')[0]
    meli_host = meli.split('@')[1]
    assert meli_user[:3] == 'zun'
    assert meli_pass[:3] == 'sit'
    assert meli_host[:4] == 'http'

    # production mode
    meli = str(MeliInterface('prod'))
    meli_user = meli.split(':')[0]
    meli_pass = meli.split(':')[1].split('@')[0]
    meli_host = meli.split('@')[1]
    assert meli_user[:3] == 'zun'
    assert meli_pass[:3] == 'sit'
    assert meli_host[:4] == 'http'

def test_get_token_access():
    meli = MeliInterface()
    token = meli.get_token_access()
    assert len(token) >= 10

def test_get_all_products_id():
    meli = MeliInterface()
    products = meli.get_all_products_id()
    assert len(products) > 0
    #  print(products)

def test_get_products_from_ids():
    meli = MeliInterface()
    products_id = meli.get_all_products_id()[:4]
    products = meli.get_products_from_ids(products_id)
    assert len(products_id) == len(products)
    
def test_get_all_products():
    meli = MeliInterface()
    products = meli.get_all_products()
    assert len(products) > 0
    # first key
    key = next(iter(products))
    assert key.startswith('MLB')
    assert products[key]['id'].startswith('MLB')
