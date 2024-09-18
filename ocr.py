import pytesseract
import cv2


def image_to_text(image_path):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # 이미지 읽기
    image = cv2.imread(image_path)

    # 이미지를 그레이스케일로 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 노이즈 제거를 위한 임계값 처리
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # OCR 수행

    text = pytesseract.image_to_string(thresh, lang='jpn')
    print(text)
    return text
