import os
import cv2
import pytesseract

# Configure the path to tesseract executable
if os.name == 'nt':  # For Windows
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define the path to the folder containing the tile images
folder_path = './tiles'

def extract_text_from_images(folder):
    for file_name in os.listdir(folder):
        img_path = os.path.join(folder, file_name)
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert image to RGB

        # Optionally preprocess image here (e.g., resizing, thresholding)
        # img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        # img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]

        text = pytesseract.image_to_string(img)
        print(f"Detected text in {file_name}: {text.strip()}")

extract_text_from_images(folder_path)