#!/usr/bin/env bash
# -s see prints
# -v more verbose

pytest ./test_util.py -sv

# pytest ./test_zunka.py -k check_zunka_products_consistence -sv
# pytest ./test_zunka.py -k get_one_product -sv
pytest ./test_zunka.py::TestProducts::test_get_all_products_with_meli_id -sv
