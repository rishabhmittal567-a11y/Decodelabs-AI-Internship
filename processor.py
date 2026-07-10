import cv2
import numpy as np

def clean_image(img_array):
    # 1. Convert to Grayscale
    if len(img_array.shape) == 3:
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    else:
        gray = img_array
    
    # 2. Apply a Median Blur to remove small noise artifacts
    blurred = cv2.medianBlur(gray, 3)
    
    # 3. Apply Adaptive Thresholding
    # This ignores the background color/gradient and focuses on the local contrast of the letters
    binary = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY, 11, 2
    )
    return binary