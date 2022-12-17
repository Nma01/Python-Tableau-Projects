# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

# --- Opening files in python
data = pd.read_csv('transaction.csv', sep=';')

# summary of data
data.info()

# Naming variables
cost_per_item = 11.73
selling_price_per_item = 21.11
number_of_items_purchased = 6
profit_per_item = selling_price_per_item - cost_per_item


# Calculations
cost_per_transaction = cost_per_item  * number_of_items_purchased 
selling_price_per_transaction = number_of_items_purchased * selling_price_per_item
profit_per_transaction = number_of_items_purchased * profit_per_item


# To Single out columns ---> variable = dataframe['column_name']

cost_per_item = data['CostPerItem']
number_of_items_purchased = data['NumberOfItemsPurchased']
cost_per_transaction = cost_per_item  * number_of_items_purchased 



selling_price_per_item = data['SellingPricePerItem']
selling_price_per_transaction = selling_price_per_item  * number_of_items_purchased



# Adding a new column to a dataframe ---> dataframe['column_name'] = variable

# ----- Calculation of cost per transaction ----
# data['CostPerTransaction'] = cost_per_transaction   or 
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']



# ---- Calculation of sales per transaction ----
# data['SalesPerTransaction'] = selling_price_per_transaction or 
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']


# ---- Calculation of profit = sales - cost ----
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']


# ---- Calculation of markup = (sales - cost)/cost ----
data['Markup'] =  data['ProfitPerTransaction'] / data['CostPerTransaction'] 


# --- round() function ---
data['round_markup'] = round(data['Markup'], 2)


# ---Cleaning/Merging date columns ---

# --- Changing day, year columns data type  to string --- 
day = data['Day'].astype(str)
year = data['Year'].astype(str)

my_date = day + '-' + data['Month'] + '-' + year

# --- This adds the new Date column to our dataframe
data['Date'] = my_date


# --- Using split function to split columns ---> new_var = column.str.split('sep'), expand=True
split_col = data['ClientKeywords'].str.split(',' , expand=True)

# --- creating & adding new columns to the dataframe (after spliting has been done) ---
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['ClientLengthOfContract'] = split_col[2]


# --- Using replace function to replace things in your data fields ---
data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['ClientLengthOfContract'] = data['ClientLengthOfContract'].str.replace(']' , '')

# --- using lower function to change items to lowercase ---
data['ItemDescription'] = data['ItemDescription'].str.lower()


# --- Bringing in a new dataset in tableau

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')


# --- Merging files in tableau (df = dataframe,key=common factor in both df's) ---> merge_df = pd.merge(old_df, new_df, on='key')
data = pd.merge(data, seasons, on='Month')
 
 
 # --- Deleting unwanted columns in dataframe using drop() function ---> df = df.drop('column_name', axis=1)
data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Year', 'Month'], axis = 1)  # --- dropping multiple items


# Exporting dataframe to csv
data.to_csv('ValueInc_Cleaned.csv', index = False) # --- index = False means ignore the index col created by python

