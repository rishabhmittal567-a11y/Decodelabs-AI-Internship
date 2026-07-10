import streamlit as st
import easyocr
import numpy as np
from PIL import Image
from src.processor import clean_image

# 1. Page Configuration
st.set_page_config(page_title="AI Text Recognizer", layout="centered")
st.title("OCR Recognition App")

# 2. File Uploader
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "png", "jpeg"])

# 3. Model Loading (Cached)
@st.cache_resource
def get_reader():
    return easyocr.Reader(['en'], gpu=False)

if uploaded_file is not None:
    # Display the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    if st.button('Recognize Text'):
        with st.spinner('AI is processing and reading the image...'):
            img_array = np.array(image)
            
            # Apply preprocessing
            processed_img = clean_image(img_array)
            
            # Load Reader and perform detection
            # paragraph=True helps group the book title correctly
            reader = get_reader()
            results = reader.readtext(processed_img, paragraph=True)
            
            st.write("### Results:")
            if not results:
                st.warning("No text detected. Try a clearer, high-contrast image.")
            else:
                # Results with paragraph=True return a list of (bbox, text)
                for (bbox, text) in results:
                    st.success(text)
