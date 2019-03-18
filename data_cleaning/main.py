from articles_cleaning import clean_articles
from locations_cleaning import clean_locations
import pandas as pd

def copy(path):
    data = pd.read_csv('../data/data_raw/'+path)
    data.to_csv('../data/data_cleaned/'+path, index=False, encoding='utf8')

def remove_spaces_and_parentheses_in_column_names():
    file_paths = ["Articles.csv", "Sales.csv", "Location.csv", 'Market_Data.csv', "Stock.csv"]
    for file_path in file_paths:
        data = pd.read_csv('../data/data_cleaned/'+file_path)
        column_names = data.columns.tolist()
        for column_name in column_names:
            if ' ' in column_name:
                data = data.rename(columns={column_name: '_'.join(column_name.split(' ')).replace('(', '').replace(')', '')})
        data.to_csv("../data/data_cleaned/"+file_path, index=False, encoding='utf8')


clean_articles()
clean_locations()
copy('Sales.csv')
copy('Stock.csv')
copy('Market_Data.csv')
remove_spaces_and_parentheses_in_column_names()