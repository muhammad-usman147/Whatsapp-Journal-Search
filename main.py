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
    print(search_object.dataframe)

    


if __name__ == '__main__':
    main()