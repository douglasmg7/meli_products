#!/usr/bin/env bash

# Must run in the current shell enviromnent.
[[ $0 != -bash ]] && echo Usage: . $BASH_SOURCE && exit 1

echo "Deactivating conda env..."
conda deactivate
# echo "Using $(python --version)"

# Stop container and docker:
echo "Stoping zunka_mongo container..."
docker stop zunka_mongo &> /dev/null
echo "Stoping zunka_redis container..."
docker stop zunka_redis &> /dev/null

# if [[ `systemctl status docker | awk '/Active/{print $2}'` == active ]] 
# then
    # echo "Stoping docker..."
    # sudo systemctl stop docker
# fi
