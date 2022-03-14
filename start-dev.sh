#!/usr/bin/env bash

# Must run in the current shell enviromnent.
[[ $0 != -bash ]] && echo Usage: . $BASH_SOURCE && exit 1

# Needed envs.
[[ -z "$ZUNKA_DOCKER_SCRIPTS" ]] && printf "[script-start-development] [error]: ZUNKA_DOCKER_SCRIPTS enviorment not defined.\n" >&2 && exit 1 

echo "Activating conda env meli_products..."
conda activate meli_products

# Start dockerizeds.
$ZUNKA_DOCKER_SCRIPTS/start-mongo.sh
$ZUNKA_DOCKER_SCRIPTS/start-redis.sh
