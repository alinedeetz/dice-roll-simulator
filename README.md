[![Build Status](https://img.shields.io/docker/cloud/build/alineem/dice-roll)](https://hub.docker.com/repository/docker/alineem/dice-roll/builds) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# Dice Rolling Simulator 

A Python based dice roller that can roll dices from 4 to 20 sides. The results are stored in a PostgreSQL database and displayed for the user on a table.

## How to run

#### DockerHub
In order to run this container you'll need docker installed.

##### Mandatory environment variables


> docker run -e DICE_ROLL_DB_USERNAME="username" 
> docker run -e DICE_ROLL_DB_PASSWORD="password" 
> docker run -e DICE_ROLL_DB_HOSTNAME="hostname" 
> docker run -e DICE_ROLL_DB_PORT="port" 
> docker run -e DICE_ROLL_DB_NAME="database-name" --rm -p 5000:5000 dice-roll
