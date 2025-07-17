import pickle
import pandas as pd
import streamlit as st
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=776df12d3fddfecb0df41af4d0d4248a&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
movie_dict=pickle.load(open('movie_dict.pkl', 'rb'))
movies=pd.DataFrame(movie_dict)
similarity= pickle.load(open('similarity.pkl', 'rb'))
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances=similarity[movie_index]
    movies_list= sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:9]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

st.image("logo.jpg", width=90)
st.title('BingeBuddy- Your Movie Recommender System')
selected_movie_name = st.selectbox(
    'Enter your Current Fav Movie for our Recommendation',
    movies['title'].values
)
if st.button('Recommend'):
    names,posters =recommend(selected_movie_name)
    col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
    with col6:
        st.text(names[5])
        st.image(posters[5])
    with col7:
        st.text(names[6])
        st.image(posters[6])
    with col8:
        st.text(names[7])
        st.image(posters[7])
