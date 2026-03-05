import pickle
import streamlit as st
import requests


session = requests.Session()


@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):

    api_key = "your_api_key_here"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=591540d1c435d2bc5fc19e8d3551ea45&language=en-US"

    try:
        response = session.get(url, timeout=5)
        response.raise_for_status()  
        data = response.json()
        poster_path = data.get("poster_path")

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        return "https://via.placeholder.com/500x750?text=No+Poster"

    except Exception as e:
        return "https://via.placeholder.com/500x750?text=Error"


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters



st.set_page_config(page_title="Movie Recommender", layout="wide")
st.header('Movie Recommender System')

# Load data
try:
    movies = pickle.load(open('movies.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("Model files not found. Please check your file paths.")
    st.stop()

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie", movie_list)

if st.button('Show Recommendation'):
    with st.spinner('Fetching posters...'):
        names, posters = recommend(selected_movie)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
