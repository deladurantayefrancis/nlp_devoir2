#!/bin/bash

set +H

cat out/is_a_\[compound\]_game.txt |\
    sed -e $'s| \/ |\\\n|gi' |\
    sed -e $'s|\/|\\\n|gi' |\

    # game adjectives
    grep -vwi 'fun' |\
    grep -Evi 'a[wr]e?so?me?' |\
    grep -Evi 'goo?d' |\
    grep -Evi 'gr(eat|8)' |\
    grep -Evi 'quality' |\
    grep -Evi 're?ally' |\

    # unrelated to the type of the game
    grep -vwi 'base' |\
    grep -vwi 'core' |\
    grep -vwi 'end' |\
    grep -vwi 'game' |\
    grep -vwi 'vanilla' |\
    grep -vwi 'video' |\

    # game franchises / softwares / companies
    grep -vwi 'civ' |\
    grep -vwi 'cod' |\
    grep -vwi 'creed' |\
    grep -vwi 'fallout' |\
    grep -vwi 'portal' |\
    grep -vi 'star ?wars' |\
    grep -vwi 'steam' |\
    grep -vwi 'valve' |\

    # miscellanous
    grep -Evi 'acc?esss?' |\
    grep -Evi '^ing' |\
    grep -Evi '^fav' |\
    grep -Evi '[td]((h|j)i?|ih?)s' |\
    grep -Evi 'the' |\
    grep -Ewvi 'type' |\
    grep -Pvi '\.' |\

    # too short or bad entries
    grep -Evi '^.{,2}$' |\
    grep -Evi '^\S\s' |\
    grep -Evi '^[^a-z]{2}' |\

    tr '[[:upper:]]' '[[:lower:]]' |\
    sort |\
    uniq > pattern4_cleaned
