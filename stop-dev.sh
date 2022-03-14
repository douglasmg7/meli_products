#!/usr/bin/env bash

# Must run in the current shell enviromnent.
[[ $0 != -bash ]] && echo Usage: . $BASH_SOURCE && exit 1

echo "Deactivating conda env..."
conda deactivate
# echo "Using $(python --version)"

# Start dockerizeds.
$ZUNKA_DOCKER_SCRIPTS/stop-mongo.sh
$ZUNKA_DOCKER_SCRIPTS/stop-redis.sh

# if [[ `systemctl status docker | awk '/Active/{print $2}'` == active ]] 
# then
    # echo "Stoping docker..."
    # sudo systemctl stop docker
# fi
