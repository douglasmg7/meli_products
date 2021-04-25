#!/usr/bin/env python
import sys
import logging

FORMAT = '%(asctime)s.%(msecs)06d %(name)s [%(levelname)s] %(message)s'
DATEFMT = '%Y/%m/%d %H:%M:%S'
logging.basicConfig(level=logging.DEBUG, format=FORMAT, datefmt = DATEFMT, filename='meli_products.log')

logging.addLevelName(logging.DEBUG, 'debug')
logging.addLevelName(logging.INFO, 'info')
logging.addLevelName(logging.WARN, 'warning')
logging.addLevelName(logging.ERROR, 'error')
logging.addLevelName(logging.CRITICAL, 'critical')

log = logging.getLogger('[meli]')
log.addHandler(logging.StreamHandler(sys.stdout))

debug = log.debug
info = log.info
warning = log.warning
error = log.error
critical = log.critical

log.debug('Debug message')
log.info('Info message')
log.warning('Warning message')
log.error('Error message')
log.critical('Critical message')
