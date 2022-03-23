#!/usr/bin/env bash
# -s see prints
# -v more verbose

# Examples.
# pytest ./test_zunka.py -k check_zunka_products_consistence -sv
# pytest ./test_zunka.py -k get_one_product -sv
# pytest ./test_zunka.py::TestProducts::test_get_all_products_with_meli_id -sv


# # All tests.
# # Util.
# pytest ./test_util.py -sv

# # Meli.
# pytest ./test_meli.py::TestMeliAuth -sv
# pytest ./test_meli.py::TestMeliProducts -sv

# # Zunka.
# pytest ./test_zunka.py::TestZunka -sv
# pytest ./test_zunka.py::TestConsistenceZunka -sv
# pytest ./test_zunka.py::TestConsistenceMeli -sv


# New testes.
pytest ./test_zunka.py::TestConsistenceMeli -sv

