#!/usr/bin/python3
""" Train the model and encode it
"""

import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                          os.pardir))
PARSED_RECIPE = os.path.join(parent_dir, 'input', 'final_parsed_recipe.csv')
TDIDF_MODEL = os.path.join(parent_dir, 'input', 'final_tdidf_model')
TDIDF_ENCODING = os.path.join(parent_dir, 'input', 'final_tdidf_encoding')

df = pd.read_csv(PARSED_RECIPE)
df['parsed_ingredients'] = df.parsed_ingredients.values.astype('U')

tfidf = TfidfVectorizer()
tfidf.fit(df['parsed_ingredients'])
tfidf_recipe = tfidf.transform(df['parsed_ingredients'])

# save the vector(tdidf model) and encoding
with open(TDIDF_MODEL, 'wb') as file:
    pickle.dump(tfidf, file)

with open(TDIDF_ENCODING, 'wb') as file:
    pickle.dump(tfidf_recipe, file)
