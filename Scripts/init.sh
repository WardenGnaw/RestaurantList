#!/bin/bash
OSINFO=$(head -1 /etc/os-release)
OSINFO=${OSINFO##*=}

if [ "$OSINFO" = "Ubuntu" ]
then
   sudo apt-get update
   sudo apt-get install python3-pip python3-dev nginx
   sudo pip3 install virtualenv
   sudo ln -s RestaurantList.service /etc/systemd/system/RestaurantList.service
   sudo systemctl start RestaurantList
   sudo systemctl enable RestaurantList
   sudo ln -s RestaurantList.nginx /etc/nginx/sites-avaliable/RestaurantList
   sudo ln -s /etc/nginx/sites-available/RestaurantList /etc/nginx/sites-enabled
   sudo systemctl restart nginx
   sudo ufw allow 'Nginx Full'
fi
