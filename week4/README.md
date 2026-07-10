AI Text Recognition (OCR) App - Week 4
A modular web application that extracts text from images using **Streamlit** and **EasyOCR**. This project is part of an AI internship, focusing on building a deployable pipeline with image preprocessing to handle real-world challenges like glare, shadows, and stylized fonts.

🚀 Features

Web Interface: Interactive dashboard using Streamlit to upload and analyze images.

Advanced Preprocessing: Uses Median Blurring and Adaptive Thresholding (via OpenCV) to clean images before recognition.

Intelligent Grouping: Uses paragraph-mode detection to group text blocks logically for better readability.

Confidence Filtering: Filters out low-confidence detections to ensure accuracy.

🛠 Tech Stack

Python 3.x

Streamlit (Web UI)

EasyOCR (Text Extraction)

OpenCV (Image Preprocessing)

🧠 How it Works

The application follows a robust preprocessing pipeline to maximize OCR accuracy:

Input: User uploads an image file (JPG/PNG).

Cleaning (src/processor.py): The image is converted to grayscale, median-blurred to reduce noise, and processed via adaptive thresholding to eliminate lighting gradients.

Recognition: The clean image is passed to the EasyOCR engine with paragraph grouping enabled.

Output: The extracted, grouped text is displayed in the dashboard.

🌐 Deployment

This project is deployed using Streamlit Cloud. To deploy your own version:

Connect your GitHub repository to Streamlit Cloud.

In the deployment settings, set the App file path to week4/app.py.
