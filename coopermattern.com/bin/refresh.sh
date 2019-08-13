#!/bin/bash
set -x
/usr/bin/python3 /var/www/coopermattern.com/flightdata.py
/usr/bin/python3 /var/www/coopermattern.com/webpage.py
echo "xd"
