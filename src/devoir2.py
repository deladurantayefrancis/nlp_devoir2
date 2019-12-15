import spacy
from spacy.symbols import nsubj, attr, dobj, PRON, DET
from tqdm import tqdm
import os
from itertools import product
import numpy as np
import re

""" sudo python -m spacy download en_core_web_sm """


nlp = spacy.load('en_core_web_lg')


os.makedirs('out', exist_ok=True)

with open('data/cleaned.txt', 'r') as file:
	reviews = file.readlines()


def find_pattern(reviews, find_dep, head_text, other_text, other_dep, filename):
	path = f'out/{filename}'
	with open(path, 'w') as file:
		for i, review in enumerate(tqdm(reviews)):
			rev = nlp(review.strip())

			find, other = [], []
			for token in rev:
				if token.head.text in head_text:
					if token.dep_ == find_dep and token.text != other_text:
						find.append(token)
					elif token.dep_ == other_dep and token.text == other_text:
						other.append(token)
			
			for f, o in product(find, other):
				if f.head == o.head and f.pos not in [PRON, DET]:
					find_text = ''.join([t.text_with_ws for t in f.subtree]).strip()
					if other_text not in find_text.lower():
						print(find_text)
						file.write(find_text + '\n')
						break


def find_pattern_chain(reviews, find_dep, head_text, headhead_text, filename):
	path = f'out/{filename}'
	with open(path, 'w') as file:
		for i, review in enumerate(tqdm(reviews)):
			rev = nlp(review.strip())

			find = []
			for token in rev:
				if token.head.text in head_text and token.head.head.text in headhead_text:
					if token.dep_ == find_dep:
						find.append(token)
			
			for f in find:
				if f.pos not in [PRON, DET]:
					find_text = ''.join([t.text_with_ws for t in f.subtree]).strip()
					print(find_text)
					file.write(find_text + '\n')


# find game names
find_pattern(reviews, find_dep='nsubj', head_text=['is'], other_text='game', other_dep='attr', filename='[nsubj]_is_a_game.txt')
find_pattern(reviews, find_dep='compound', head_text=['franchise', 'series'], other_text='the', other_dep='det', filename='the_[compound]_(franchise/series).txt')
find_pattern_chain(reviews, find_dep='pobj', head_text=['like'], headhead_text=['game', "it's"], filename="(game_like/it's_like)_[pobj].txt")

# find types and adjectives
find_pattern_chain(reviews, find_dep='compound', head_text=['game'], headhead_text=['is'], filename='is_a_[compound]_game.txt')
