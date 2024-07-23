import fitz  # PyMuPDF
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os
import pandas as pd
from PyPDF2 import PdfReader


class preprocess_text:
    def __init__(self):
        return
    
    def OCR(self,pdf_path):
        try:
            images=convert_from_path(pdf_path,dpi=300) #pdfを画像に変換
            text=''
            
            #各画像に対しOCRを行いtextとして獲得
            for i, image in enumerate(images):
                temp_image_path = f'page_{i}.png'
                image.save(temp_image_path, 'PNG')  # 画像ファイルとして一時保存
    
                text += pytesseract.image_to_string(Image.open(temp_image_path), lang='eng')  # OCRを実行
                os.remove(temp_image_path) # 一時画像ファイルを削除

            return text
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    
    
    def save_text(self,text,text_file_name):
        with open(text_file_name,'w') as f:
            f.write(text)
            print(f'{text_file_name}にテキストを保存しました')
        
        return
    
    def read_text(self,text_file_name):
        with open(text_file_name,'r') as f:
            text=f.read()
        
        return text
    
    def one_words(self,text):
        delate_words={".":None, "," : None,":" : None,";" : None,"!" : None,'"' :None,"#" :None,"$" :None,"%" :None,"&" :None,"'" :None,'"':None,"(" :None,")" :None,"=" :None,"~" :None,"{" :None,"}" :None,"[" :None,"]" :None,"/":None,"-":None,"_":None,"^":None}
        table=str.maketrans(delate_words)
        text=text.lower()
        text=text.translate(table)
        one_words=text.split()
        
        return one_words
    
    def two_words(self,text):
        delate_words={".":None, "," : None,":" : None,";" : None,"!" : None,'"' :None,"#" :None,"$" :None,"%" :None,"&" :None,"'" :None,'"':None,"(" :None,")" :None,"=" :None,"~" :None,"{" :None,"}" :None,"[" :None,"]" :None,"/":None,"-":None,"_":None,"^":None}
        table=str.maketrans(delate_words)
        text=text.lower()
        text=text.translate(table)
        words=text.split()
        words.append('<pad>')  #下のfor文においてone_wordsとの系列帳を合わせるために追加
        
        two_words=[]
        for i in range(len(words)-1):
            two_words.append(words[i]+' '+words[i+1])

        return two_words
    
    def three_words(self,text):
        delate_words={".":None, "," : None,":" : None,";" : None,"!" : None,'"' :None,"#" :None,"$" :None,"%" :None,"&" :None,"'" :None,'"':None,"(" :None,")" :None,"=" :None,"~" :None,"{" :None,"}" :None,"[" :None,"]" :None,"/":None,"-":None,"_":None,"^":None}
        table=str.maketrans(delate_words)
        text=text.lower()
        text=text.translate(table)
        words=text.split()
        words.append('<pad>')  #下のfor文においてone_wordsとの系列帳を合わせるために追加
        words.append('<pad>')

        three_words=[]
        for i in range(len(words)-2):
            three_words.append(words[i]+' '+words[i+1]+' '+words[i+2])

        return three_words
    
    def four_words(self,text):
        delate_words={".":None, "," : None,":" : None,";" : None,"!" : None,'"' :None,"#" :None,"$" :None,"%" :None,"&" :None,"'" :None,'"':None,"(" :None,")" :None,"=" :None,"~" :None,"{" :None,"}" :None,"[" :None,"]" :None,"/":None,"-":None,"_":None,"^":None}
        table=str.maketrans(delate_words)
        text=text.lower()
        text=text.translate(table)
        words=text.split()
        words.append('<pad>')  #下のfor文においてone_wordsとの系列帳を合わせるために追加
        words.append('<pad>')
        words.append('<pad>')

        four_words=[]
        for i in range(len(words)-3):
            four_words.append(words[i]+' '+words[i+1]+' '+words[i+2]+' '+words[i+3])

        return four_words




