import pandas as pd
import pickle as pk
import requests             # Library used for hitting the API

movies_df = pd.Dataframe(pk.load(open('movies.pkl', 'rb')))
movies_similarity = pd.Dataframe(pk.load(open('movie_similarity.pkl', 'rb')))

def get_poster(id):
    response = requests.get(f"....{id}......")
    data = response.json()

    # return the poster path of the given movie
    initial_poster_path = ""
    return initial_poster_path + data['poster_path']


def recommend(movie, n_movies=5):

    """ Given a movie name, it returns the list of
        the top (n_movies = 5) movie NAMES and
         POSTERS similar to the given movie, as 2 lists    """

    # fetch the movie index
    index = movies_df[movies_df['title'] == movie].index[0]

    # fetch the similarity array of the corresponding movie
    similarities = movies_similarity[index]

    to_recommend_list = sorted(list(enumerate(similarities)), reverse=True, key=lambda x: x[1])[1:(n_movies + 1)]
    to_recommend_movies = []
    to_recommend_movie_posters = []

    for movie in to_recommend_list:
        movie_index = movie[0]
        to_recommend_movies.append(movies_df.iloc[movie_index].title)
        movie_id = movies_df.iloc[movie_index].movie_id
        # Fetch poster using API by movie_id
        to_recommend_movie_posters.append(get_poster(movie_id))

    return to_recommend_movies, to_recommend_movie_posters
