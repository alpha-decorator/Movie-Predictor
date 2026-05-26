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

/* ---------------- MAIN APP ---------------- */

.stApp {
    background: linear-gradient(
        135deg,
        #0f0c29,
        #302b63,
        #24243e
    );

    color: #f5deb3;
    overflow-x: hidden;
}

/* ---------------- TITLE ---------------- */

.title {

    text-align: center;
    font-size: 65px;
    color: #FFD700;
    font-weight: bold;

    text-shadow:
        0px 0px 10px rgba(255,215,0,0.7),
        0px 0px 20px rgba(255,215,0,0.5);

    margin-bottom: 10px;

    animation: glow 2s infinite alternate;
}

@keyframes glow {

    from {
        text-shadow:
            0px 0px 10px rgba(255,215,0,0.7);
    }

    to {
        text-shadow:
            0px 0px 25px rgba(255,215,0,1);
    }
}

/* ---------------- SUBTITLE ---------------- */

.subtitle {

    text-align: center;
    font-size: 22px;
    color: #e6d3a3;

    margin-bottom: 35px;
}

/* ---------------- SELECTBOX ---------------- */

div[data-baseweb="select"] > div {

    background-color: rgba(30,27,75,0.85);

    border-radius: 14px;

    color: white;

    border: 1px solid rgba(255,255,255,0.1);

    backdrop-filter: blur(8px);
}

/* ---------------- BUTTON ---------------- */

.stButton > button {

    width: 100%;

    background: linear-gradient(
        to right,
        #6a11cb,
        #2575fc
    );

    color: white;

    border-radius: 15px;

    height: 3em;

    font-size: 20px;

    font-weight: bold;

    border: none;

    transition: all 0.4s ease;

    box-shadow:
        0px 0px 15px rgba(106,17,203,0.5);
}

.stButton > button:hover {

    transform: scale(1.05);

    background: linear-gradient(
        to right,
        #ff512f,
        #dd2476
    );

    box-shadow:
        0px 0px 25px rgba(255,81,47,0.8);
}

/* ---------------- IMAGE CARDS ---------------- */

[data-testid="stImage"] {

    overflow: hidden;

    border-radius: 18px;

    transition: all 0.4s ease;

    cursor: pointer;
}

[data-testid="stImage"]:hover {

    transform: scale(1.08);

    box-shadow:
        0px 0px 30px rgba(255,215,0,0.8);

    z-index: 999;
}

/* ---------------- MOVIE TITLE ---------------- */

.movie-title {

    text-align: center;

    font-size: 18px;

    color: #ffe082;

    margin-top: 12px;

    font-weight: bold;

    transition: 0.3s ease;
}

.movie-title:hover {

    color: white;

    transform: scale(1.05);
}

/* ---------------- RESPONSIVE ---------------- */

@media screen and (max-width: 900px) {

    .title {
        font-size: 42px;
    }

    .subtitle {
        font-size: 18px;
    }
}

</style>
""", unsafe_allow_html=True)
# ---------------------------------------------------
# FETCH POSTER
# ---------------------------------------------------

def fetch_poster(movie_id):

    return (
        "https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c"
    )
# https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c
# ---------------------------------------------------
# RECOMMEND FUNCTION
# ---------------------------------------------------

def recommend(movie):

    movie_index = movies[
        movies['title'] == movie
    ].index[0]

    distances = cosine_similarity(
        vectors[movie_index],
        vectors
    )[0]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in movies_list:

        recommended_movie_names.append(
            movies.iloc[i[0]].title
        )

        recommended_movie_posters.append(
            fetch_poster(i[0])
        )

    return (
        recommended_movie_names,
        recommended_movie_posters
    )


# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

movies = pickle.load(
    open('movies_dict.pkl', 'rb')
)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

cv = CountVectorizer(
    max_features=5000,
    stop_words='english'
)

vectors = cv.fit_transform(
    movies['tags']
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
        st.image(recommended_movie_posters[0],use_container_width=True)
        st.markdown(
            f"<div class='movie-title'>{recommended_movie_names[0]}</div>",
            unsafe_allow_html=True
        )

    with col2:
        st.image(recommended_movie_posters[1],use_container_width=True)
        st.markdown(
            f"<div class='movie-title'>{recommended_movie_names[1]}</div>",
            unsafe_allow_html=True
        )

    with col3:
        st.image(recommended_movie_posters[2],use_container_width=True)
        st.markdown(
            f"<div class='movie-title'>{recommended_movie_names[2]}</div>",
            unsafe_allow_html=True
        )

    with col4:
        st.image(recommended_movie_posters[3],use_container_width=True)
        st.markdown(
            f"<div class='movie-title'>{recommended_movie_names[3]}</div>",
            unsafe_allow_html=True
        )

    with col5:
        st.image(recommended_movie_posters[4],use_container_width=True)
        st.markdown(
            f"<div class='movie-title'>{recommended_movie_names[4]}</div>",
            unsafe_allow_html=True
        )