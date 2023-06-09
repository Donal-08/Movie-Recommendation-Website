import streamlit as st
import pickle as pk
import pandas as pd
from helper import recommend

# # 'movies.pkl' is a dictionary
movies_df = pd.Dataframe(pk.load(open('movies.pkl', 'rb')))
# movies_similarity = pd.Dataframe(pk.load(open('movie_similarity.pkl', 'rb')))

# Check Streamlit documentation
st.title('Movie Recommender System')

# Display a select widget for movie names
selected_movie = st.selectbox('Recommend movies similar to', movies_df['title'].values)

# Add a button for recommend
if(st.button('Recommend')):
    movie_names, movie_posters = recommend(selected_movie)

    # Display the movie names and posters column-wise
    c1, c2, c3, c4, c5 = st.beta_columns(5)
    with c1:
        st.text(movie_names[0])
        st.image(movie_posters[0])
    with c2:
        st.text(movie_names[1])
        st.image(movie_posters[1])
    with c3:
        st.text(movie_names[2])
        st.image(movie_posters[2])
    with c4:
        st.text(movie_names[3])
        st.image(movie_posters[3])
    with c5:
        st.text(movie_names[4])
        st.image(movie_posters[4])




