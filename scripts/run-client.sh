#!/bin/sh

set -e

# Go to root folder
cd $(dirname $0)/..

NAME="Distributed-Auction-System"
PROJECT_DIR="${PWD}/auction_system"
MODULE_NAME="client/Home.py"

echo "Starting ${NAME} client..."

streamlit run ${PROJECT_DIR}/${MODULE_NAME} --server.port 8501
