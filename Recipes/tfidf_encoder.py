import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# load in parsed recipe dataset
df_recipes = pd.read_csv('dataset/parsed_data.csv')

# Tfidf needs unicode or string types
df_recipes['NER_parsed'] = df_recipes.NER_parsed.values.astype('U')

# TF-IDF feature extractor
tfidf = TfidfVectorizer()
tfidf.fit(df_recipes['NER_parsed'])
tfidf_recipe = tfidf.transform(df_recipes['NER_parsed'])

# save the tfidf model and encodings
with open('tfidf.pkl', "wb") as f:
     pickle.dump(tfidf, f)
with open('tfidf_encodings.pkl', "wb") as f:
     pickle.dump(tfidf_recipe, f)