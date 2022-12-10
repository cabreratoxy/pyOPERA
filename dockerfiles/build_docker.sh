#!/bin/bash
docker build -t cabreratoxy/pyopera:0.${CIRCLE_BUILD_NUM}.0 -f dockerfiles/Dockerfile
docker push cabreratoxy/pyopera:0.${CIRCLE_BUILD_NUM}.0
