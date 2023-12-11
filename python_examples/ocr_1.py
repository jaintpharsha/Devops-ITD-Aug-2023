from PIL import Image
import pytesseract


# Specify Tesseract executable location if not in PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(img)

    return text


# Replace 'your_image.png' with the path to your image file
image_path = 'any_image_with.png'
extracted_text = extract_text_from_image(image_path)

print(extracted_text)
