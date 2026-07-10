import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# --- 1. Page Configuration ---
# 'initial_sidebar_state="expanded"' forces the sidebar to stay open
st.set_page_config(
    page_title="AI Data Doctor", 
    layout="centered", 
    initial_sidebar_state="expanded"
)
st.title("🩺 AI Data Doctor & Classifier")

# --- 2. Sidebar Uploader ---
st.sidebar.header("Data Loading")
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

# --- 3. Loading Logic (No Fallback) ---
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state['df'] = df
    st.sidebar.success(f"Loaded: {uploaded_file.name}")
else:
    # If no file is uploaded, clear session and stop execution
    if 'df' in st.session_state:
        del st.session_state['df']
    st.info("Please upload a CSV file in the sidebar to begin.")
    st.stop() 

# --- 4. Processing & Audit ---
df = st.session_state['df']

with st.expander("🔍 View Data Audit"):
    st.write("### Missing Values")
    st.write(df.isnull().sum())
    df = df.fillna(0) # Simple auto-clean

st.write("### Data Preview", df.head())

# --- 5. Model Configuration ---
target_col = st.selectbox("Select the Target Column (what to predict):", df.columns)

# Preprocessing: Convert categorical data to numbers
processed_df = df.copy()
for col in processed_df.select_dtypes(include=['object', 'category']).columns:
    processed_df[col] = LabelEncoder().fit_transform(processed_df[col].astype(str))

if st.button("🚀 Train Model"):
    X = processed_df.drop(columns=[target_col], errors='ignore')
    y = processed_df[target_col]
    
    # Build and train
    model = RandomForestClassifier()
    model.fit(X, y)
    
    st.success("Model trained successfully!")
    
    # --- 6. Feature Importance ---
    st.write("### Key Factors (Feature Importance)")
    importances = pd.Series(model.feature_importances_, index=X.columns)
    st.bar_chart(importances)