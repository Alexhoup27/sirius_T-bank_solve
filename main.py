import pandas as pd
class Model():
  def __init__(self, movies_data:pd.DataFrame, users_data:pd.DataFrame):
    self.movies = movies_data
    self.users = users_data
    self.keys_users = users_data['Unnamed: 0']
    self.keys_movies = movies_data['Unnamed: 0'].to_list()
  def predict(self, movie_id, user_id):
    answ = 0
    count = 0
    for _key, movie_key in zip(self.users['Unnamed: 0'], self.users[user_id].values):
      if movie_key != 0:  
        _val = self.movies[movie_id][self.keys_movies.index(f'{_key}{movie_key}')]
      else:
        continue
      if _val != 0:
        count += 1
        answ += _val
    return answ / count if count !=0 else 0
movies_data = pd.read_csv(r'new_movie.csv')
users_data = pd.read_csv(r'new_users.csv')
model = Model(movies_data, users_data)
