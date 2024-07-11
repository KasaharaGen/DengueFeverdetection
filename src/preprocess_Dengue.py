import os
from preprocess_text import preprocess_text
from preprocess_df import preprocess_df

dir_path='../data/sample_data'

pre_text=preprocess_text()
columns=['burning micturition','cold','craniocaudal','mediolateral']  #システム上小文字で入力するのを忘れずに
pre_df=preprocess_df(columns)##
pre_dengue_df=pre_df.make_df()
store_list=[pre_dengue_df]

for filename in os.listdir(dir_path):
    pdf_path = os.path.join(dir_path, filename)

    text=pre_text.OCR(pdf_path)
    one_words=pre_text.one_words(text)

    df=pre_df.add_labels_df(pre_dengue_df,one_words)
    store_list.append(df)

Dengue_df=pre_df.comp_df(store_list)
pre_df.make_csv(Dengue_df,'../data/Dengue2.csv')