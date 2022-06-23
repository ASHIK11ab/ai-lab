from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

import numpy as np

data = fetch_20newsgroups()

text_categories = data.target_names

train_data = fetch_20newsgroups(subset="train", categories=text_categories)

test_data = fetch_20newsgroups(subset="test", categories=text_categories)

print(len(train_data.data))
print(type(train_data.data))
print(dir(train_data.data))
input()

model = MultinomialNB()

model.fit(train_data.data, train_data.target)
predicted_categories = model.predict(test_data.data)

print(len(predicted_categories))
