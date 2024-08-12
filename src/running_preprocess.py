import os
import pandas as pd
from preprocess import preprocess_text,preprocess_df

dir_path='../data/dengue_data'

pre_text=preprocess_text()

extraction_words=['cold','craniocaudal','mediolateral','fever','cough']  #システム上小文字で入力するのを忘れずに
dir_path='../data/dengue_data'
dict_df=[]

for filename in os.listdir(dir_path):
    pdf_path = os.path.join(dir_path, filename)
    text=pre_text.OCR(pdf_path)
    jugde_dict=pre_text.extraction_words_to_dict(text,extraction_words)
    dict_df.append(jugde_dict)

df=pd.DataFrame(dict_df)

