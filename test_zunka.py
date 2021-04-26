#!/usr/bin/env python
from zunka import ZunkaInterface

def test_get_one_product():
    zunka = ZunkaInterface()
    zunka.get_one_product()
    
def test_get_all_products_with_meli_id():
    zunka = ZunkaInterface()
    zunka.get_all_products_with_meli_id()
