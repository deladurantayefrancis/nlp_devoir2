#!/bin/bash

python src/preprocess.py

cat data/reviews.txt |\
    perl -pe 's/([A-Za-z][a-z]{3,})([A-Z][a-z])/\1 \2/g' |\
    perl -pe 's/([;!?.])([^ ;!?.])/\1 \2/g' > data/cleaned.txt
