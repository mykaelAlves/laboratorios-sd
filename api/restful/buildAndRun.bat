@echo off
call mvn clean package
call docker build -t com.restful/restful .
call docker rm -f restful
call docker run -d -p 9080:9080 -p 9443:9443 --name restful com.restful/restful