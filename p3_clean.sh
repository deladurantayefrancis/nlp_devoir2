#!/bin/bash

set +H

cat out/\(game_like-it\'s_like\)_\[pobj\].txt |\
    sed -e $'s/ or /\\\n/gi' |\
    sed -e $'s/ and /\\\n/gi' |\
    sed -e $'s/ with /\\\n/gi' |\
    sed -e $'s/ but /\\\n/gi' |\
    sed -e $'s/ like /\\\n/gi' |\
    sed -e $'s/, /\\\n/gi' |\
    sed -e 's/,//gi' |\
    grep -Ev "^[^A-Z]+$" |\
    grep -Evw 'the' |\
    grep -Evw 'games?' |\
    grep -vi '^a ' |\
    grep -Evi '^.{,3}$' |\
    tr '[[:upper:]]' '[[:lower:]]' |\
    sort |\
    uniq > pattern3_cleaned
