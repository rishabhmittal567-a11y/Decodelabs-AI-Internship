import streamlit as st
import sys
import os

# 1. Path Management: Add 'week3' to the system path to ensure modules are found
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 2. Import your engine from the src following
from engine import RecommenderEngine

# 3. Cache the engine and load data using absolute paths
@st.cache_resource
def get_engine():
    # Get the directory of app.py
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the full paths to the CSV files located in 'week3/data/'
    movies_csv = os.path.join(base_path, 'data', 'movies.csv')
    ratings_csv = os.path.join(base_path, 'data', 'ratings.csv')
    
    return RecommenderEngine(movies_csv, ratings_csv)

# Initialize the engine
engine = get_engine()

# 4. Streamlit UI
st.title("🎬 Movie Recommender Pro")

user_id = st.number_input("Enter User ID", min_value=1, step=1)

if st.button("Get Recommendations"):
    try:
        # Fetch recommendations from the engine
        recs = engine.get_recommendations(user_id)
        
        st.write(f"Top 5 Recommendations for User {user_id}:")
        
        # Display as a dataframe
        st.dataframe(recs)
        
    except Exception as e:
        # Display error if something goes wrong (e.g., User ID not found)
        st.error(f"Error: {e}")
