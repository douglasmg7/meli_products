#!/usr/bin/env python
import os

def get_run_mode():
    try:
        run_mode = os.environ['RUN_MODE']
    except:
        run_mode = ''

    # production
    if run_mode.lower().startswith('prod'):
        print('Running in production mode')
        return { 'PROD': True, 'DEV': False, 'TEST': False }
    # test
    elif run_mode.lower().startswith('test'):
        print('Running in test mode')
        return { 'PROD': False, 'DEV': False, 'TEST': True }
    # development
    else:
        print('Running in development mode')
        return { 'PROD': False, 'DEV': True, 'TEST': False }
