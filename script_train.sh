#!/bin/bash

thresholds="50"
sizes="300"

python src/word2vec.py $thresholds $sizes

for t in {50..50..50}
do
    for s in {300..300..100}
    do
        folder="model_T-${t}_S-${s}"
        gzip $folder/word2vec.txt
        python -m spacy init-model en "$folder/spacy.word2vec.model" --vectors-loc "$folder/word2vec.txt.gz"
    done
done

