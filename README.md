

# Movie Recommender System

A movie recommendation web app built using Python and Streamlit.  
The system recommends similar movies based on genres, overview, cast, crew, keywords, popularity, rating and release year.

## Features

- Movie recommendations using cosine similarity
- Movie posters using TMDB API
- Harry Potter inspired UI
- Content based + hybrid recommendation system
- Streamlit web interface

## Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- TMDB API

## Files

- `app1.py` → Streamlit web app
- `movies_dict.pkl` → movie dataset
- `similarity.pkl` → similarity matrix

## Run Locally

Install dependencies:

```bash
pip install streamlit pandas scikit-learn requests
