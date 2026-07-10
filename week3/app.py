import streamlit as st
import sys
import os

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.engine import RecommenderEngine

# Load the engine (caching it saves time on page reloads)
@st.cache_resource
def get_engine():
    return RecommenderEngine('data/movies.csv', 'data/ratings.csv')

engine = get_engine()

st.title("🎬 Movie Recommender Pro")

user_id = st.number_input("Enter User ID", min_value=1, step=1)

if st.button("Get Recommendations"):
    try:
        recs = engine.get_recommendations(user_id)
        st.write(f"Top 5 Recommendations for User {user_id}:")
        st.dataframe(recs) # This displays a nice, sortable table
    except Exception as e:
        st.error(f"Error: {e}")