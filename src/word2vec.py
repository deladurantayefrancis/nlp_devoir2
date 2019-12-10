import os
import pandas as pd
import spacy
import sys
import time
import spacy

from tqdm import tqdm

from gensim import models, parsing, utils
from gensim.models.phrases import Phrases, Phraser

"""
# command line arguments
thresholds, sizes = sys.argv[1], sys.argv[2]

thresholds = [int(t) for t in thresholds.split(',')]
sizes = [int(s) for s in sizes.split(',')]
"""

threshold, size = int(sys.argv[1]), int(sys.argv[2])


with open('data/reviews.txt', 'r') as file:
	sentences = file.readlines()

#sentences = [utils.simple_preprocess(sent) for sent in tqdm(sentences)]
sentences = [parsing.preprocessing.strip_multiple_whitespaces(
	parsing.preprocessing.strip_punctuation(sent)
) for sent in tqdm(sentences)]


start = time.time()
phrases = Phrases(sentences, threshold=threshold)
bigram = Phraser(phrases)
sents = [bigram[sent] for sent in sentences]
print(f'bigram_{threshold}:', time.time() - start)

start = time.time()
phrases = Phrases(sents, threshold=10)
trigram = Phraser(phrases)
sents = [trigram[sent] for sent in sentences]
print(f'trigram_10:', time.time() - start)

FOLDER = f'model_T-{threshold}_S-{size}'
os.makedirs(FOLDER, exist_ok=True)
start = time.time()
model = models.Word2Vec(sentences=sents, size=size)
model.wv.save_word2vec_format(f'{FOLDER}/word2vec.txt')
print(f'word2vec_{size}:', time.time() - start)
