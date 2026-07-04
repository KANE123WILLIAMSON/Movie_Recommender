import streamlit as st
import pandas as pd
import pickle

st.title("Movie Recommender")

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity_2.pkl', 'rb'))

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['original_title'] == movie].index[0]

    recommended_movies = []

    for idx in similarity[movie_index]:
        recommended_movies.append(
            movies.iloc[idx]['original_title']
        )

    return recommended_movies[:5]
# Dropdown
option = st.selectbox(
    "Select your movie",
    movies['original_title'].values
)

# Button
if st.button("Recommend"):
    recommendations = recommend(option)

    for movie in recommendations:
        st.write(movie)