#!/bin/bash
 
[[ -z "$MERCADO_LIVRE_PATH" ]] && printf "[meli-timer] [error]: MERCADO_LIVRE_PATH enviorment not defined.\n" >&2 && exit 1 

while true
do
    RUN_MODE=production conda run -n meli_products $MERCADO_LIVRE_PATH/app.py

    # One minute.
    # sleep 60

    # One hour
    sleep 3600
done