import glob 
from FileSearch import Search
import textwrap
class Details():
    def __init__(self):
        self.by = None
        self.id = None
        self.keyword = None



FILES_DIR = ''
FILES_TYPE = '.csv'
def main():
    #Creating Search Object
    search_object = Search()

    #creating DataFrames
    df_list = glob.glob(f'{FILES_DIR}*{FILES_TYPE}')
    ret, _ = search_object.CreateDataFrames(df_list=df_list,FILE_NAME = 'converted.csv')


    #--- Search By ISSN and eISSN
    by = input("Search By [ISSN, eISSN, both]? ")
    id = input("Enter ID: ")
    
    output = search_object.SearchByID(id,by)
    print(output.strip())
    # output = search_object.SearchByKeyword('plant')
    # if len(output) > 1500:
    #     sub_outputs = output.split("--"*10 )
    #     for i in sub_outputs:
    #         print(i)
    # print(len(output))


if __name__ == '__main__':
    main()