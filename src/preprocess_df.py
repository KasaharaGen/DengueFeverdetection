import pandas as pd

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