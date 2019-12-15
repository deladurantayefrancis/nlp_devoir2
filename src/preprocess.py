import demjson
import json
import pandas as pd
import re
import ast

from tqdm import tqdm


labels = ['user_id', 'item_id', 'funny', 'helpful_yew', 'helpful_total', 'recommend', 'review']

file_in = 'data/australian_user_reviews.json'
file_out = 'data/reviews.json'


content = []
with open(file_in, 'r') as json_in:
	for line in tqdm(json_in):
		content.append(ast.literal_eval(line))

with open(file_out, 'w+') as json_out:
	json.dump(content, json_out)

with open(file_out, 'r') as file:
	content = json.load(file)


with open('data/reviews.txt', 'w') as txt_file:
	with open('data/reviews.csv', 'w') as csv_file:
		for entry in tqdm(content):
			for review in entry['reviews']:
				if review['funny'] != '':
					funny = review['funny'].split()[0]
				else:
					funny = 0
				if review['helpful'] != 'No ratings yet':
					helpful_words = review['helpful'].split()
					helpful_yes = helpful_words[0]
					helpful_total = helpful_words[2]
				else:
					helpful_yes = 0
					helpful_total = 0
				line = [entry['user_id'], review['item_id'], funny, helpful_yes, helpful_total, review['recommend'], review['review']]
				csv_file.write('\t'.join(list(map(str, line))) + '\n')
				txt_file.write(review['review'].strip() + '\n')

