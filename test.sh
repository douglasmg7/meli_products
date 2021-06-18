#!/usr/bin/env bash
# -s see prints
# -v more verbose

pytest ./test_zunka.py -k check_zunka_products_consistence -sv
