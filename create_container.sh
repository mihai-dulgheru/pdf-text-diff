#!/bin/bash

# Start Docker daemon
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  # Linux
  sudo systemctl start docker
fi

# Build the Docker image
docker build -t my-python-app .

# Create and run the Docker container
docker run -d --name my-python-container -p 5000:5000 my-python-app
