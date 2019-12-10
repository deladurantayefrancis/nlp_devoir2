import spacy
from spacy.symbols import nsubj, attr, dobj, PRON
from tqdm import tqdm


""" sudo python -m spacy download en_core_web_sm """


nlp = spacy.load('en_core_web_sm')

with open('data/reviews.txt', 'r') as file:
	reviews = file.readlines()


"""
doc = nlp('Splinter cell, a game from my infancy, is a very good game')
#doc = nlp('Splinter cell, a game from my infancy, is a very bad time')

nsubjs = []
attrs = []
for token in doc:
	if token.dep == nsubj and token.head.text == 'is':
		nsubjs.append(token)
	if token.dep == attr and token.text == 'game' and token.head.text == 'is':
		attrs.append(token)

for chunk in doc.noun_chunks:
	for subject in nsubjs:
		for att in attrs:
			if subject.head == att.head and subject in chunk.subtree:
				print(chunk.text)
"""

def tqdm(something):
	return something

for i, review in enumerate(tqdm(reviews)):
	rev = nlp(review)
	for entity in rev.ents:
		if entity.label_ in ['ORG', 'PERSON', 'PRODUCT']:
			print(entity.label_, '-', entity.text)
			print(rev)
	if i > 100:
		break

"""
with open('res', 'w') as file:

	for i, review in enumerate(tqdm(reviews)):
		rev = nlp(review)
		
		nsubjs, attrs = [], []
		for token in rev:
			if token.dep == nsubj and token.head.text in ['is', 'was']:
				nsubjs.append(token)
			if token.dep == attr and token.text == 'game' and token.head.text in ['is', 'was']:
				attrs.append(token)

		for chunk in rev.noun_chunks:
			for subject in nsubjs:
				for att in attrs:
					if subject.head == att.head and subject in chunk.subtree and subject.pos != PRON and chunk.text.lower() != 'this game':
						#print('GAME:', chunk.text)
						file.write(chunk.text + '\n')
						#print(chunk.text)
						#print(reviews[i])
"""
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
