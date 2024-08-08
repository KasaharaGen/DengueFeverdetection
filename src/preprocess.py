import fitz  # PyMuPDF
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os
import pandas as pd
from collections import Counter
import re



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

            delate_words={".":None, "," : None,":" : None,";" : None,"!" : None,'"' :None,"#" :None,"$" :None,"%" :None,"&" :None,"'" :None,'"':None,"(" :None,")" :None,"=" :None,"~" :None,"{" :None,"}" :None,"[" :None,"]" :None,"/":None,"-":None,"_":None,"^":None,"@":None}
            table=str.maketrans(delate_words)
            text=text.lower()
            text=text.translate(table)
            text=text.split()
            text=" ".join(text)

            return text
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        
    
    #text内の特徴量の判別
    def extraction_words_to_dict(self,text, extraction_words):
        jugde_dict = {}
        
        for item in extraction_words:
            jugde_dict[item] = 1 if item in text else 0
        
        return jugde_dict
    
    
class preprocess_df:
    def __init__(self,columns):
        self.columns=columns
        return
    
    def first_make_df(self):
        df=pd.DataFrame(columns=self.columns)
        return df
    
    def make_labels_df(self,df,text):
        new_data={}   
        for column in self.columns:
            new_data[column] = 1 if re.search(re.escape(column), text) else 0
        label_df=pd.DataFrame([new_data])
        df=pd.concat([df,label_df],ignore_index=True)
        return df
    
    def comp_df(self,store_list):
        Dengue_df=pd.concat(store_list,ignore_index=True)
        Dengue_df.index.name='patientID'
        return Dengue_df 
    
    def make_comp_df(self,one_words_Dengue_df,two_words_Dengue_df,three_words_Dengue_df,four_words_Dengue_df):
        Dengue_df=pd.merge(one_words_Dengue_df,two_words_Dengue_df,on='patientID',how='left')
        Dengue_df=pd.merge(Dengue_df,two_words_Dengue_df,on='patientID',how='left')
        Dengue_df=pd.merge(Dengue_df,three_words_Dengue_df,on='patientID',how='left')
        Dengue_df=pd.merge(Dengue_df,four_words_Dengue_df,on='patientID',how='left')
        return Dengue_df

    def make_csv(self,Dengue_df,save_path_name):
        Dengue_df.to_csv(save_path_name,index=True)
        return




