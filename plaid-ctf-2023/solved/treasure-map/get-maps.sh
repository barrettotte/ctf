#!/bin/bash

maps_url=http://treasure.chal.pwni.ng/

mkdir -p maps

for i in {0..199}
do
    echo $i
    curl -O --output-dir ./maps $maps_url/$i.js.map

    # sourcemapper -url $maps_url/$i.js.map -output src
done