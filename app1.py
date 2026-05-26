import pickle
import streamlit as st
import requests

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="🧙 Magical Movie Recommender",
    page_icon="🪄",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS (Harry Potter Theme)
# ---------------------------------------------------

st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(to bottom, #0f0c29, #302b63, #24243e);
    color: #f5deb3;
}

/* Header */
.title {
    text-align: center;
    font-size: 60px;
    color: #FFD700;
    font-weight: bold;
    text-shadow: 3px 3px 10px black;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 22px;
    color: #e6d3a3;
    margin-bottom: 30px;
}

/* Selectbox */
div[data-baseweb="select"] > div {
    background-color: #1e1b4b;
    color: white;
    border-radius: 12px;
}

/* Button */
.stButton > button {
    width: 100%;
    background: linear-gradient(to right, #6a11cb, #2575fc);
    color: white;
    border-radius: 15px;
    height: 3em;
    font-size: 20px;
    font-weight: bold;
    border: none;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.05);
    background: linear-gradient(to right, #ff512f, #dd2476);
}

/* Movie title */
.movie-title {
    text-align: center;
    font-size: 18px;
    color: #ffe082;
    margin-top: 10px;
    font-weight: bold;
}

/* Poster styling */
img {
    border-radius: 15px;
    box-shadow: 0px 0px 15px rgba(255,215,0,0.5);
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# FETCH POSTER
# ---------------------------------------------------

def fetch_poster(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"

    data = requests.get(url)
    data = data.json()

    poster_path = data['poster_path']

    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path

    return full_path


# ---------------------------------------------------
# RECOMMEND FUNCTION
# ---------------------------------------------------

def recommend(movie):

    index = movies[movies['title'] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:

        movie_id = movies.iloc[i[0]].movie_id

        recommended_movie_posters.append(
            fetch_poster(movie_id)
        )

        recommended_movie_names.append(
            movies.iloc[i[0]].title
        )

    return recommended_movie_names, recommended_movie_posters


# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

movies = pickle.load(
    open('movies_dict.pkl', 'rb')
)

similarity = pickle.load(
    open('similarity.pkl', 'rb')
)

# ---------------------------------------------------
# HEADER SECTION
# ---------------------------------------------------

st.markdown(
    '<div class="title">🧙 Magical Movie Recommender</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Discover movies through magic ✨</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------
# SELECT MOVIE
# ---------------------------------------------------

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "🎬 Choose your magical movie",
    movie_list
)

# ---------------------------------------------------
# RECOMMENDATION BUTTON
# ---------------------------------------------------

if st.button('✨ Reveal Recommendations'):

    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(recommended_movie_posters[0])
        st.markdown(
            f"<div class='movie-title'>{recommended_movie_names[0]}</div>",
            unsafe_allow_html=True
        )

    with col2:
        st.image(recommended_movie_posters[1])
        st.markdown(
            f"<div class='movie-title'>{recommended_movie_names[1]}</div>",
            unsafe_allow_html=True
        )

    with col3:
        st.image(recommended_movie_posters[2])
        st.markdown(
            f"<div class='movie-title'>{recommended_movie_names[2]}</div>",
            unsafe_allow_html=True
        )

    with col4:
        st.image(recommended_movie_posters[3])
        st.markdown(
            f"<div class='movie-title'>{recommended_movie_names[3]}</div>",
            unsafe_allow_html=True
        )

    with col5:
        st.image(recommended_movie_posters[4])
        st.markdown(
            f"<div class='movie-title'>{recommended_movie_names[4]}</div>",
            unsafe_allow_html=True
        )