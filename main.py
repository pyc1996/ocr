from gemini import trans_jp_to_kr
from ocr import image_to_text

if __name__ == '__main__':
    text = image_to_text("./image/1726411961.jpg")
    trans_jp_to_kr(text)
