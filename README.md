# dockerAIO

This script uses the Docker daemon to send docker-related commands to a remote docker server listening on a specified port.

## Features
- list all containers on remote docker server
- stop specified container
- start specified container
- create new container
  - currently only creates ubuntu container with mounted host file system (used for red team)
