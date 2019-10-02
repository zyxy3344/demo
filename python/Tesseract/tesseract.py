__author__ = "紫羽"

import pytesseract
from PIL import Image

image = Image.open("1.png")
text = pytesseract.image_to_string(image)
print(text)


