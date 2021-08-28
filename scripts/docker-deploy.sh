#!/usr/bin/env bash

cd /~app

# Pulling  the changes

git checkout main;

git pull origin main;

# Docker

docker-compose up -d --build

exit 0;