#!/usr/bin/env bash

# Must run in the current shell enviromnent.
[[ $0 != -bash ]] && echo Usage: . $BASH_SOURCE && exit 1

echo "Deactivating conda env..."
conda deactivate
echo "Using $(python --version)"

# [[ `systemctl status mongodb | awk '/Active/{print $2}'` == inactive ]] && sudo systemctl start mongodb
# [[ `systemctl status redis | awk '/Active/{print $2}'` == inactive ]] && sudo systemctl start redis
# [[ `systemctl status nginx | awk '/Active/{print $2}'` == inactive ]] && sudo systemctl start nginx
# exit 0
