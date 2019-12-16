#!/bin/bash

set +H

cat out/the_\[compound\]_\(franchise-series\).txt |\
    grep -vi 'game' |\
    grep -vwi 'sci' |\
    grep -vwi 'television' |\
    grep -vwi 'movie' |\
    grep -vwi 'anime' |\
    grep -Evi '^.{,3}$' |\
    tr '[[:upper:]]' '[[:lower:]]' |\
    sort |\
    uniq > pattern2_cleaned
