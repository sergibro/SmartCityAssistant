#!/bin/bash
APP_PATH="$( cd "$( dirname "$0" )" && cd ../ && pwd )"
CONTAINER_NAME="sca"
COMMAND="docker/daemon.sh"

sudo docker stop $CONTAINER_NAME
sudo docker rm $CONTAINER_NAME
sudo docker run \
    -d \
    --restart always \
    -e TZ=Europe/Kiev \
    --name $CONTAINER_NAME \
    -v $APP_PATH:/app \
    sergibro/tg-bots \
    $COMMAND