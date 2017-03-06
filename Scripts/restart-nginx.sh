#!/bin/bash
# This script needs to be run if there are any changes to RestaurantList.nginx
sudo nginx -t
sudo nginx -s reload
sudo systemctl restart nginx
