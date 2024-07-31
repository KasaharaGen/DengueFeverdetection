import os
from preprocess import preprocess_text,preprocess_df

dir_path='../data/dengue_data'

pre_text=preprocess_text()
#columns=(colomnsの単語数×それぞれのcolumns)の2次元配列
columns=['cold','craniocaudal','mediolateral','fever','cough']  #システム上小文字で入力するのを忘れずに
pre_df=preprocess_df(columns)
pre_dengue_df=pre_df.first_make_df()
store_list=[pre_dengue_df]

for filename in os.listdir(dir_path):
    pdf_path = os.path.join(dir_path, filename)

    text=pre_text.OCR(pdf_path)

    df=pre_df.make_labels_df(pre_dengue_df,text)
    store_list.append(df)

Dengue_df=pre_df.comp_df(store_list)
pre_df.make_csv(Dengue_df,'../data/Dengue.csv')