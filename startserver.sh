#!/bin/bash
docker build -t finitive-socket-server:latest .
docker run --rm -it --name=finitive-notif --net=host finitive-socket-server:latest