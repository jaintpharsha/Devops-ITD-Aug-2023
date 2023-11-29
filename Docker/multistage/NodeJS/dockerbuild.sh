#!/bin/sh
echo Building nodewebapp from Dockerfile.dev

docker build -t nodewebapp:v1 -f Dockerfile.dev .

echo Creating Conatiner Out of Image
docker container create --name extract nodewebapp:v1
docker container cp extract:/usr/src/app/WebApp/dist ./dist
docker container rm -f extract

echo Building nodewebapp version 2

docker build --no-cache -t nodewebapp:v2 .
rm ./dist