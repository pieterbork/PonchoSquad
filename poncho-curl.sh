#!/bin/bash
ARGS=""
for i
do
    ARGS="$ARGS $i"
done
curl --data "apikey=4837b1adf0d071cd02bd05953d59b3e20ff48bcccea185b37f2bc2a63fcc73d7&url=$i" https://www.virustotal.com/vtapi/v2/url/scan
echo "This url is being checked"
