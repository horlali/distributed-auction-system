#!/bin/sh

set -e

# Go to root folder
cd $(dirname $0)/..

NAME="Distributed-Auction-System"
PROJECT_DIR="${PWD}/auction_system"
MODULE_NAME="server/main.py"

echo "Starting ${NAME} server..."

python ${PROJECT_DIR}/${MODULE_NAME}
