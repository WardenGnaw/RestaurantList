#!/usr/bin/env bash
# This script is intended to be used for development/test builds.
GITROOT=$(git rev-parse --show-toplevel)
echo $GITROOT
mkdir -p $GITROOT/.setup-files
printf "USERNAME=test\nPASSWORD=test\nDATABASE=RestaurantListTest\nHOST=localhost\n" > $GITROOT/.setup-files/mysql
mysql -u root -p < $GITROOT/Scripts/create-test-user.sql
