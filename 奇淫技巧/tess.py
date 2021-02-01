from PIL import Image
import pytesseract
 
text = pytesseract.image_to_string(Image.open('E:\\1-26.jpg'))
print(text)