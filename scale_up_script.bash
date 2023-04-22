#!/bin/bash
if [ -f "./docker-compose.yml" ]
then
    docker-compose up --scale app1=3 -d --build
fi