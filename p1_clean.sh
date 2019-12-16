#!/bin/bash

set +H

cat out/\[nsubj\]_is_a_game.txt |\
    perl -pe 's/ ?\(.+\) ?//g' |\
    perl -pe 's/,.+//g' |\
    perl -pe 's/review //gi' |\
    perl -pe 's/overall //gi' |\
    perl -pe 's/overview - //gi' |\
    perl -pe 's/[0-9]+([[:punct:]][0-9]+)? //gi' |\
    grep -iE '[a-z]' |\
    grep -vwi 'this' |\
    grep -vwi 'that' |\
    grep -vwi 'all' |\
    grep -vwi 'i' |\
    grep -Pvi "((?!i)[a-z])\1{2,}" |\
    grep -Ev "^[Tt]he (only )?[a-z]\S+$" |\
    grep -vi '/' |\
    grep -vi '*' |\
    grep -vi '^a ' |\
    grep -Pvi "(?!['-.:&])[[:punct:]]" |\
    grep -Evi '^.{,3}$' |\
    grep -Evi '([[:punct:]].*){4,}' |\
    # tr '[[:upper:]]' '[[:lower:]]' |\
    sort |\
    uniq > pattern1_cleaned
    # uniq -c |\
    # sort -k1,1nr > pattern1_cleaned
