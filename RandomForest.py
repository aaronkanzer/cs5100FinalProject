from sklearn import datasets
import pandas as pd
import ast
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from collections import Counter

data = pd.read_csv('./train.csv')
print(data.shape)

for col in ['genres', 'production_companies', 'spoken_languages', 'Keywords', 'cast', 'crew']:
    data[col] = data[col].apply(lambda x: {} if pd.isna(x) else ast.literal_eval(x))

genre_col = data['genres']
# print(genre_col)
# list_of_genres = list(genre_col.apply(lambda x: [i['name'] for i in x] if x != {} else []).values)

list_of_genres = list(data['genres'].apply(lambda x: [i['name'] for i in x] if x != {} else []).values)
# print(list_of_genres)
print(Counter([i for j in list_of_genres for i in j]).most_common())
# data['genres'].apply(lambda x: len(x) if x != {} else 0).value_counts()

# genre_types = list(data['genres'].apply(lambda x: [i['name'] for i in x] if x != {} else []).values)
# print(genre_types)
