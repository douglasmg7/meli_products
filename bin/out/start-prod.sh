#!/usr/bin/env bash

# Must run in the current shell enviromnent.
[[ $0 != -bash ]] && echo Usage: . $BASH_SOURCE && exit 1

# Needed envs.
[[ -z "$MERCADO_LIVRE_PATH" ]] && printf "[script-start-meli-production] [error]: MERCADO_LIVRE_PATH enviorment not defined.\n" >&2 && exit 1 

# echo "Activating conda env meli_products..."
conda activate meli_products
$MERCADO_LIVRE_PATH/app.py
conda deactivate
