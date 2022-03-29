#! /usr/bin/env bash

# Remove link for all user access.
if [[ -f /usr/local/bin/meli ]]; then
    echo Removing link for allnations...
    sudo rm /usr/local/bin/meli
fi

# Remove meli timer and service.
if systemctl list-units --full --all | grep -Fq "meli.timer"; then
    echo Removing timer...
    sudo systemctl stop meli.timer 
    sudo systemctl disable meli.timer 
    sudo rm -v /lib/systemd/system/meli.timer
    echo Removing service...
    sudo rm -v /lib/systemd/system/meli.service
    sudo systemctl daemon-reload
    sudo systemctl reset-failed
else
    echo No meli timer installed.
fi
