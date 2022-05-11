import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('a1.csv',encoding='utf8')
df = df[df['text_y'].notna()]

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df['text_y'])
cosine_sim = cosine_similarity(count_matrix,count_matrix)

df = df.reset_index()
indices = pd.Series(df.index,index = df['title_y'])


def get_recommendations(title) :
  idx = indices[title]
  sim_scores = list(enumerate(cosine_sim[idx]))
  sim_scores = sorted(sim_scores,key = lambda x: x[1],reverse = True)
  sim_scores = sim_scores[1:11]
  movie_indices = [i[0] for i in sim_scores]
  return df.iloc[movie_indices].values.tolist()
