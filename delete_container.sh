#!/bin/bash

# Stop and remove the Docker container
docker stop my-python-container
docker rm -v my-python-container

# Remove the Docker image
docker rmi my-python-app

# Remove all unused containers, networks, images, and volumes
docker system prune -af
