#!/bin/bash

arg1="$1"

if [ "$arg1" = "up" ]; then
    echo "Starting ROS2 !............."
    echo "Allowing X11 forward to display GUI.."
    xhost +local:root
    echo "Running docker compose up --build"
    docker-compose up --build -d
    echo "ROS2_linux started successfully!"
elif [ "$arg1" = "down" ]; then
    echo "Removing X11 forward access to display GUI.."
    xhost -local:root
    echo "Exiting container ....... running docker-compose down"
    docker-compose down
    echo "ROS2_linux ended successfully!"

else
    echo "Invalid Argument. Use 'up' or 'down'"
fi
