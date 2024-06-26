import fitz  # PyMuPDF
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os
import pandas as pd


class preprocess_text:
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
    
    def save_text(self,text,text_file_name):
        with open(text_file_name,'w') as f:
            f.write(text)
            print(f'{text_file_name}にテキストを保存しました')
        
        return
    
    def read_text(self,text_file_name):
        with open(text_file_name,'r') as f:
            text=f.read()
        
        return text
    
    def one_words(self,text,delate_words):
        table=str.maketrans(delate_words)
        text=text.lower()
        text=text.translate(table)
        one_words=text.split()
        
        return one_words
    
    def two_words(self,text,delate_words):
        table=str.maketrans(delate_words)
        text=text.lower()
        text=text.translate(table)
        two_words=text.split()

        corpus=[]
        for i in range(len(two_words)-2):
            corpus.append(two_words[i:i+2])

        return two_words
    
    def three_words(self,text,delate_words):
        table=str.maketrans(delate_words)
        text=text.lower()
        text=text.translate(table)
        three_words=text.split()
        
        corpus=[]
        for i in range(len(three_words)-3):
            corpus.append(three_words[i:i+3])

        return three_words
    
    def four_words(self,text,delate_words):
        table=str.maketrans(delate_words)
        text=text.lower()
        text=text.translate(table)
        four_words=text.split()
        
        corpus=[]
        for i in range(len(four_words)-4):
            corpus.append(four_words[i:i+4])

        return four_words
    


class preprocess_df:
    def __init__(self,columns):
        self.columns=columns
        return
    
    def make_df(self):
        df=pd.DataFrame(columns=self.columns)

        return df
    
    def add_labels_df(self,df,words):
        new_data={column:0 for column in self.columns}
        pre_df=pd.DataFrame([new_data])

        for column in self.columns:
            for token in words:
                if column==token:
                    pre_df[column]=1
        
        df=pd.concat([df,pre_df],ignore_index=True)
        
        return df
    
    def comp_df(self,store_list):
        Dengue_df=pd.concat(store_list,ignore_index=True)
        Dengue_df.index.name='patient ID'
        return Dengue_df 
    
    def make_csv(self,Dengue_df):
        Dengue_df.to_csv('Dengue.csv',index=True)
        return


