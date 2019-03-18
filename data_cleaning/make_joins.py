import pandas as pd
############################################################################
# Execute this file to make all possible joins of the tables in input_path #
############################################################################

input_path = '../data/data_raw/'
output_path = '../data/data_cleaned/'

#Keys name :
location_key = 'Location (Code)'
item_key = 'Item (Code)'


def delete_column_with_regex(df, regex):
    df = df[df.columns.drop(list(df.filter(regex=regex)))]
    return df

# Load all tables and set primary index if it exists
print('\nLoading csv...\nLocation.csv')
Location = pd.read_csv(input_path+'Location.csv')
Location.set_index('Location (Code)', verify_integrity=True)

print('Articles.csv')
Articles = pd.read_csv(input_path+'Articles.csv')
Articles.set_index('Item (Code)', verify_integrity=True)

print('Market_Data.csv')
Market_Data = pd.read_csv(input_path+'Market_Data.csv')
print('Sales.csv')
Sales = pd.read_csv(input_path+'Sales.csv')
print('Stock.csv\n')
Stock = pd.read_csv(input_path+'Stock.csv')


# Jointures :
print('Joining tables...\n')
Sales_Location = Sales.merge(Location, on=[location_key], how='outer', suffixes=('', '_to_delete'))
Sales_Location = delete_column_with_regex(Sales_Location, '_to_delete')

MarketData_Location = Market_Data.merge(Location, on=[location_key], how='outer', suffixes=('', '_to_delete'))
MarketData_Location = delete_column_with_regex(MarketData_Location, '_to_delete')

Sales_Articles = Sales.merge(Articles, on=[item_key], how='outer', suffixes=('', '_to_delete'))
Sales_Articles = delete_column_with_regex(Sales_Articles, '_to_delete')

Sales_Articles_Location = Sales_Articles.merge(Location, on=[location_key], how='outer', suffixes=('', '_to_delete'))
Sales_Articles_Location = delete_column_with_regex(Sales_Articles_Location, '_to_delete')

# print(Stock)
# Stock_Articles = Stock.merge(Articles, on=[item_key], how='outer', suffixes=('', '_to_delete'))
# Stock_Articles = delete_column_with_regex(Stock_Articles, '_to_delete')
#
# Stock_Location = Stock.merge(Location, on=[location_key], how='outer', suffixes=('', '_to_delete'))
# Stock_Location = delete_column_with_regex(Stock_Location, '_to_delete')
#
# Stock_Articles_Location = Stock_Articles.merge(Location, on=[location_key], how='outer', suffixes=('', '_to_delete'))
# Stock_Articles_Location = delete_column_with_regex(Stock_Articles_Location, '_to_delete')



# Save joins
print('Saving...\nSales_Location.csv')
Sales_Location.to_csv(output_path+'Sales_Location.csv',index=False)
print('MarketData_Location.csv')
MarketData_Location.to_csv(output_path+'MarketData_Location.csv',index=False)
print('Sales_Articles.csv')
Sales_Articles.to_csv(output_path+'Sales_Articles.csv',index=False)
print('Sales_Articles_Location.csv')
Sales_Articles_Location.to_csv(output_path+'Sales_Articles_Location.csv',index=False)
# print('Stock_Articles.csv')
# Stock_Articles.to_csv(output_path+'Stock_Articles.csv',index=False)
# print('Stock_Location.csv')
# Stock_Location.to_csv(output_path+'Stock_Location.csv',index=False)
# print('Stock_Articles_Location.csv')
# Stock_Articles_Location.to_csv(output_path+'Stock_Articles_Location.csv',index=False)
