import pandas as pd 
import numpy as np 
import os 

class Search():
    def __init__(self):
        self.dataframe = pd.DataFrame({})  

    def CreateDataFrames(self,df_list:list,FILE_NAME:str):
        if isinstance(df_list,list) and isinstance(FILE_NAME,str):
            try: 
                if os.path.exists(FILE_NAME):
                    #if <FILENAME> exists, will load the file directly
                    print(f"[INFO]: {FILE_NAME} already exists..")
                    print(f"[INFO]: Loading {FILE_NAME}")
                    self.dataframe = pd.read_csv(FILE_NAME)
                    return True, None
                else:
                    #otherwise, create the DataFrame and save it as <FILENAME>
                    df = pd.DataFrame({})
                    for i in df_list:
                        df = pd.concat([df,pd.read_csv(i)],axis=0)
                    df.to_csv(FILE_NAME,index=False)
                    self.dataframe = df
                    return True, None
            except Exception as e:
                #if by chance any error occurs
                return False, str(e)
        else:
            raise TypeError(f"Expected Inputs as <list> and <str>")
            
