#!/bin/bash

# Build Docker image
docker build -t my-places-db .
# Run Docker container
docker run --name my-place-db-container -d -p 5432:5432 my-places-db
