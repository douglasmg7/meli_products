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
