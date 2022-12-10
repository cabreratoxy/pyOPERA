#!/bin/bash
docker build -t cabreratoxy/pyopera:0.${CIRCLE_BUILD_NUM}.0 .
docker push -t cabreratoxy/pyopera:0.${CIRCLE_BUILD_NUM}.0
