#!/bin/sh
if [ $(docker ps -a -f name=restful | grep -w restful | wc -l) -eq 1 ]; then
  docker rm -f restful
fi
mvn clean package && docker build -t com.restful/restful .
docker run -d -p 9080:9080 -p 9443:9443 --name restful com.restful/restful
