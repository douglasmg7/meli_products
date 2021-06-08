#!/usr/bin/env python
from zunka import ZunkaInterface, loadDic
from meli import MeliInterface

def test_get_one_product():
    zunka = ZunkaInterface()
    product = zunka.get_one_product()
    
def test_get_all_products_with_meli_id():
    zunka = ZunkaInterface()
    products = zunka.get_all_products_with_meli_id()
    assert len(products) > 0
    # get the first key
    first_item = next(iter(products))
    # must be a mongo id
    assert len(first_item) == 24
    # must have meli id
    assert products[first_item]['mercadoLivreId'].startswith('MLB')

    #  print(first_item)
    #  print(products[first_item]['mercadoLivreId'])

# Each zunka product that have a not empty mercadoLivreId,
# must have a associated meli product that have a seller_custom_field
# if associated zunka product _id.
def test_check_zunka_meli_products_consistence():
    zunka = ZunkaInterface()
    #  zunka_products = zunka.get_all_products_with_meli_id()
    zunka_products = loadDic('./json/zunka_products.json')
    # First zunka product.
    zunka_product_id = next(iter(zunka_products))

    meli = MeliInterface()
    #  meli_products = meli.get_all_products()
    meli_products = loadDic('./json/meli_products.json')

    result = zunka.check_zunka_meli_products_consistence(zunka_products, meli_products)
    print(f'id: {zunka_product_id}')
    assert zunka_product_id in result['no_meli_product']
    #  print(result)
