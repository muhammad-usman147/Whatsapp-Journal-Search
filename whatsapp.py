import glob 
from FileSearch import Search


FILES_DIR = ''
FILES_TYPE = '.csv'
def main():
    #Creating Search Object
    search_object = Search()

    #creating DataFrames
    df_list = glob.glob(f'{FILES_DIR}*{FILES_TYPE}')
    ret, _ = search_object.CreateDataFrames(df_list=df_list,FILE_NAME = 'converted.csv')


    #--- Search By ISSN and eISSN
    #by = input("Search By [ISSN, eISSN, both]? ")
    #id = input("Enter ID: ")
    
    #output = search_object.SearchByID(id,by)
    #print(output)
    print(search_object.SearchByKeyword('english'))



if __name__ == '__main__':
    main()