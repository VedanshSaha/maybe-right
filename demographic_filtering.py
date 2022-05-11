import pandas as pd
import numpy as np

df = pd.read_csv('a1.csv')

C = df["contentId"].mean()
m = df['authorSessionId_x'].quantile(0.9)
q_movies = df.copy().loc[df['authorSessionId_x']>=m]

def weighted_rating(x,m = m,C=C) :
  V = x['authorSessionId_x']
  R = x['contentId']
  return ((V / (V+m)) * R + (m / (V+m)) * C)

q_movies['score'] = q_movies.apply(weighted_rating,axis=1)

q_movies = q_movies.sort_values('score',ascending= False)
output = q_movies.head(20).values.tolist()

