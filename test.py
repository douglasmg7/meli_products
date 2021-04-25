#!/usr/bin/env python
from meli import MeliInterface
from zunka import ZunkaInterface

def test_meli_zunka_auth_envs():
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

def test_meli_get_token_access():
    meli = MeliInterface()
    token = meli.get_token_access()
    assert len(token) >= 10

def test_meli_list_all_products():
    meli = MeliInterface()
    products = meli.list_all_products()
    print(products)

def test_meli_get_products():
    meli = MeliInterface()
    products_id = meli.list_all_products()
    products = meli.get_products(products_id)
    assert len(products_id) == len(products)

def test_meli_log():
    meli = MeliInterface()
    meli.log()

def test_zunka_get_one_product():
    zunka = ZunkaInterface()
    zunka.get_one_product()
    
def test_zunka_get_all_products_with_meli_id():
    zunka = ZunkaInterface()
    zunka.get_all_products_with_meli_id()


if __name__ == '__main__':
    #  test_meli_zunka_auth_envs()
    #  test_meli_get_token_access()
    #  test_meli_list_all_products()
    #  test_meli_get_products()
    #  test_zunka_get_all_products_with_meli_id()
    test_zunka_get_one_product()
    test_meli_log()
