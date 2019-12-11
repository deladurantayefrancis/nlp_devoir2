import spacy
from spacy.symbols import nsubj, attr, dobj, PRON, DET
from tqdm import tqdm
import os
from itertools import product
import numpy as np

""" sudo python -m spacy download en_core_web_sm """


nlp = spacy.load('en_core_web_lg')


os.makedirs('out', exist_ok=True)

with open('data/cleaned.txt', 'r') as file:
	reviews = file.readlines()


def find_pattern(reviews, find_dep, head_text, other_text, other_dep):
	"""
	def tqdm(something):
		return something
	"""
	path = f'out/[{find_dep}]_{head_text}_{other_text}[{other_dep}]'

	with open(path, 'w') as file:

		for i, review in enumerate(tqdm(reviews)):
			rev = nlp(review)

			find, other = [], []
			for token in rev:
				if token.head.text == head_text:
					if token.dep_ == find_dep and token.text != other_text:
						find.append(token)
					elif token.dep_ == other_dep and token.text == other_text:
						other.append(token)
			
			for chunk, f, o in product(rev.noun_chunks, find, other):
				if f.head == o.head and f.pos not in [PRON, DET]:
					if f in chunk.subtree:
						to_write = ' '.join([t.text for t in f.subtree])
						file.write(to_write + '\n')
						break


def find_pattern_chain(reviews, find_dep, head_text, headhead_text):
	"""
	def tqdm(something):
		return something
	"""
	path = f'out/[{find_dep}]_{headhead_text}_{head_text}'

	with open(path, 'w') as file:

		for i, review in enumerate(tqdm(reviews)):
			rev = nlp(review)

			find = []
			for token in rev:
				if token.head.text == head_text and token.head.head.text == headhead_text:
					if token.dep_ == find_dep:
						find.append(token)
			
			for chunk, f in product(rev.noun_chunks, find):
				if f.pos not in [PRON, DET]:
					if f in chunk.subtree:
						to_write = ' '.join([t.text for t in f.subtree])
						file.write(to_write + '\n')
						break


find_pattern(reviews, find_dep='nsubj', head_text='is', other_text='game', other_dep='attr')
find_pattern(reviews, find_dep='compound', head_text='franchise', other_text='the', other_dep='det')
find_pattern_chain(reviews, find_dep='pobj', head_text='like', headhead_text='game')
#find_pattern(reviews, find_dep='compound', head_text='franchise', other_text='the', other_dep='det')


find_pattern_chain(reviews, find_dep='compound', head_text='game', headhead_text='is')

"""
nsubjs, attrs = [], []
for token in rev:
	if token.dep == nsubj and token.head.text == 'like':
		nsubjs.append(token)
	if token.dep == dobj and token.head.text == 'like':
		attrs.append(token)

for chunk in rev.noun_chunks:
	for subject in nsubjs:
		for att in attrs:
			if subject.head == att.head and att in chunk.subtree:
				print('GAME:', chunk.text)
				print(reviews[i])

"""

#if i > 500:
#	break
