import pickle
import streamlit as st
import pandas as pd
from huggingface_hub import hf_hub_download
import pickle


st.header('Movie Recommender System')
movies = pickle.load(open('model/movie_dict.pkl','rb'))
movies = pd.DataFrame(movies)


if "similarity" not in st.session_state:
    # Download the file
    file_path = hf_hub_download(
        repo_id="AbhayUrmaliya2004/Movie_Recommendation_System2",
        filename="similarity.pkl",
        repo_type="model"
    )

    # Load the file using pickle
    with open(file_path, "rb") as f:
        st.session_state.similarity = pickle.load(f)



def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(st.session_state.similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []

    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names



movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movies = recommend(selected_movie)

    for movie in recommended_movies:
        st.write(movie)
    

