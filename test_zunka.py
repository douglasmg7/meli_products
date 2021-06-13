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

    meli = MeliInterface()
    meli_products = loadDic('./json/meli_products.json')

    # No mercadoLivreId.
    zunka_products = loadDic('./json/zunka_product_no_mercado_livre_id.json')
    # First zunka product.
    zunka_product_id = next(iter(zunka_products))
    # print(f'id: {zunka_product_id}')
    result = zunka.check_zunka_meli_products_consistence(zunka_products, meli_products)
    assert zunka_product_id in result['no_meli_id']
    #  print(result)

    # No meli product.
    zunka_products = loadDic('./json/zunka_product_no_meli_product.json')
    # First zunka product.
    zunka_product_id = next(iter(zunka_products))
    # print(f'id: {zunka_product_id}')
    result = zunka.check_zunka_meli_products_consistence(zunka_products, meli_products)
    assert zunka_product_id in result['no_meli_product']
    #  print(result)

    # No back reference.
    zunka_products = loadDic('./json/zunka_product_no_back_reference.json')
    # First zunka product.
    zunka_product_id = next(iter(zunka_products))
    # print(f'id: {zunka_product_id}')
    result = zunka.check_zunka_meli_products_consistence(zunka_products, meli_products)
    assert zunka_product_id in result['no_back_reference']
    #  print(result)

    # zunka product not equal meli product.
    zunka_products = loadDic('./json/zunka_product.json')
    meli_products = loadDic('./json/meli_products_diff_title.json')
    # First zunka product.
    zunka_product_id = next(iter(zunka_products))
    # print(f'id: {zunka_product_id}')
    result = zunka.check_zunka_meli_products_consistence(zunka_products, meli_products)
    assert zunka_product_id in result['not_equal']
    print(result)
