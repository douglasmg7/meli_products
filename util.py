#!/usr/bin/env python
from logger import debug, info, warning, error, critical

import os

def get_run_mode():
    try:
        run_mode = os.environ['RUN_MODE']
    except:
        run_mode = ''

    # production
    if run_mode.lower().startswith('prod'):
        debug('Running in production mode')
        return { 'PROD': True, 'DEV': False, 'TEST': False }
    # test
    elif run_mode.lower().startswith('test'):
        debug('Running in test mode')
        return { 'PROD': False, 'DEV': False, 'TEST': True }
    # development
    else:
        debug('Running in development mode')
        return { 'PROD': False, 'DEV': True, 'TEST': False }

def obfuscate_mongo_string_connection(s: str):
    try:
        ar = s.split(':')
        sub_ar = ar[2].split('@') 
        sub_ar[0] = 'xxxx'
        ar[2] = '@'.join(sub_ar)
        r = ':'.join(ar)
        return r
    except:
        error('Could not obfuscate mongo string connection')
        return 'xxxx'
