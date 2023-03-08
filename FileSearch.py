import pandas as pd 
import numpy as np 
import os 

class JournalIDError(Exception):
    def __init__(self,message):
        self.message = message


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
                        temp_df = pd.read_csv(i)
                        index = i.split("(")[1].split(")")[0]
                        temp_df['index'] = [index for _ in range(temp_df.shape[0])]
                        df = pd.concat([df,temp_df],axis=0)
                    df.to_csv(FILE_NAME,index=False)
                    self.dataframe = df
                    return True, None
            except Exception as e:
                #if by chance any error occurs
                return False, str(e)
        else:
            raise TypeError(f"Expected Inputs as <list> and <str>")
        
    '''
    To search data with respect to ISSN or eISSN ID.
    '''

    def SearchByID(self, id:str,search_by='issn'):
        '''
        search_by = [issn, eissn]

        '''
        data = {
            'Publisher name':[],
            'Index':[],
            'Category':[]
        }
        journal_id = ['issn', 'eissn','both']
        search_by = search_by.lower()
        if search_by.lower() in journal_id:
            if search_by ==  journal_id[0]:
                #query to search by ISSN only
                results = self.dataframe.query(f"ISSN == '{id}'")
            elif search_by == journal_id[1]:
                #query to search by eISSN only
                results = self.dataframe.query(f"eISSN == '{id}'")
            elif search_by == journal_id[2]:
                results = self.dataframe.query(f"eISSN == '{id}' |eISSN == '{id}'  ")
            else:
                JournalIDError(f"The provided either ID: {id} or search_type: {search_by} is invalid ")
          
            for _,r in results.iterrows():
                    data['Publisher name'].append(r['Publisher name'])
                    data['Category'].append(r['Web of Science Categories'])
                    data['Index'].append(r['index'])
            return data
                

        else:
            raise JournalIDError("Journal ID should be either ISSN, eISSN, both")


