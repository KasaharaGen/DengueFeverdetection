import fitz  # PyMuPDF
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os

class preprocess:
    def __init__(self):
        return
    
    def OCR(self,pdf_path):
        images=convert_from_path(pdf_path,dpi=300) #pdfを画像に変換

        #各画像に対しOCRを行いtextとして獲得
        for i, image in enumerate(images):
            temp_image_path = f'page_{i}.png'
            image.save(temp_image_path, 'PNG')  # 画像ファイルとして一時保存
    
            text = pytesseract.image_to_string(Image.open(temp_image_path), lang='eng')  # OCRを実行
            os.remove(temp_image_path) # 一時画像ファイルを削除
        
        return text
    

