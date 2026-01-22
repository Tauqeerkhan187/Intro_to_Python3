# Author: TK
# Date: 22-01-2026
# Desc: Simple local program that extracts English text from an image (offline)
# Notes:
# - OpenCV handles image preprocessing.
# - Tesseract (installed locally) does the OCR.

import os
import cv2
import numpy as np
import pytesseract

TESSERACT_EXE = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = TESSERACT_EXE



# Resolve image path relative to THIS script file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_NAME = "51MhwbEN4iL.jpg"
IMG_PATH = os.path.join(BASE_DIR, IMG_NAME)

print("Resolved image path:", IMG_PATH)

# Check file exists before trying to load it
if not os.path.exists(IMG_PATH):
    raise FileNotFoundError(
        f"Image file not found at:\n{IMG_PATH}\n\n"
        f"Put '{IMG_NAME}' in the same folder as this script."
    )



# Load the image (OpenCV loads as a NumPy array in BGR format)
img = cv2.imread(IMG_PATH)
if img is None:
    raise RuntimeError(
        "OpenCV could not read the image (file may be corrupted or unsupported)."
    )

# Image dimensions: height, width
h, w = img.shape[:2]



# Crop to region where big text is likely located
# For this pic, the main headline text is in the bottom section.

crop = img[int(h * 0.55):h, 0:w]



# Preprocess for OCR
# Convert to grayscale (OCR works best on single-channel images)

gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

# Increase contrast using CLAHE (handles uneven lighting/background)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
gray = clahe.apply(gray)

# Upscale (OCR reads larger characters more accurately)

gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# Threshold to black/white using Otsu (separates text from background)

_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)



# OCR using Tesseract
# --oem 3: default OCR engine mode
# --psm 6: treat the image as a block of text

config = "--oem 3 --psm 6"

text = pytesseract.image_to_string(thresh, lang="eng", config=config)



# Output results + show debug image

print("\n===== OCR OUTPUT =====")
print(text)

cv2.imshow("OCR Preprocessed Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
