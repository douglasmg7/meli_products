#!/usr/bin/env python

import requests
import os

user_id = os.environ['MERCADO_LIVRE_USER_ID']
token_access='APP_USR-8486926819913701-041913-15722792c64956aab1b0d44c5f24971c-360790045'

def get_all_meli_products():
    url = f'https://api.mercadolibre.com/users/{user_id}/items/search'
    headers = {'Authorization': f'Bearer {token_access}'}
    r = requests.get(url, headers=headers)
    return r.json()['results']

print(get_all_meli_products())
