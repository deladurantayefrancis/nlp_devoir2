#!/bin/bash

thresholds="50"
sizes="300"

for t in {50..50..50}
do
    for s in {300..300..100}
    do
        folder="model_T-${t}_S-${s}"
        for resize in {4000..12000..4000}
        do
            python src/voisins.py $folder $resize
        done
    done
done

