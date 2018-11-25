# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 05:39:06 2018

@author: Eliud Lelerai
"""
## %%


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline


df=pd.read_csv('https://raw.githubusercontent.com/jackiekazil/data-wrangling/master/data/chp3/data-text.csv')

df.head(2)

df1=pd.read_csv('https://raw.githubusercontent.com/kjam/data-wrangling-pycon/master/data/berlin_weather_oldest.csv')

df1.head(2)

# 1. Get the Metadata from the above files

df.info()

df1.info()

# 2. Get the row names from the above files

df.values

df1.values

# 3. Change the column name from any of the above file



df.rename(columns={'Indicator':'Indicator_ID'})

# 4. Change the column name from any of the above file and store the changes made permanently

df=df.rename(columns={'Indicator':'Indicator_ID'})

# 5. Change the names of multiple columns.

df=df.rename(columns={'PUBLISH STATES':'Publication_Status','WHO region':'WHO_Region'})

# 6. Arrange values of a particular column in ascending order.

df_sorted_1=df.sort_values('Year')

# 7. Arrange multiple column values in ascending order.

df_sorted_2=df.sort_values(['Indicator_ID','WHO_Region'])

# 8. Make country as the first column of the dataframe.

df.columns

df=df[['Country','Indicator_ID', 'Publication_Status', 'Year', 'WHO_Region','World Bank income group','Sex', 'Display Value', 'Numeric','Low', 'High', 'Comments']]

# 9. Get the column array using a variable

column_array=np.array(df['WHO_Region'].values)

# 10. Get the subset rows 11, 24, 37

df_subset=df.loc[[11,24,37],:]

# 11. Get the subset rows excluding 5, 12, 23, and 56

df_subset2=df.drop([5,12,23,56])

# ***********END OF PART I*************************************************************************************


# PART II

users=pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/users.csv')
sessions=pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/sessions.csv')
products=pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/products.csv')
transactions=pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/transactions.csv')

users.head()
sessions.head()
transactions.head()

# 12. Join users to transactions, keeping all rows from transactions and only matching rows from users (left join)

leftjoin_Trans_users=pd.merge(left=transactions, right=users,how='left',on='UserID',indicator=True)

# 13. Which transactions have a UserID not in users?

outerjoin_Trans_users=pd.merge(left=transactions, right=users,how='outer',on='UserID',indicator=True)
left_only_Transusers=outerjoin_Trans_users[outerjoin_Trans_users['_merge']=='left_only']

# 14. Join users to transactions, keeping only rows from transactions and users that match via UserID (inner join)

innerjoin_Trans_users=pd.merge(left=transactions, right=users,how='inner',on='UserID',indicator=True)

# 15. Join users to transactions, displaying all matching rows AND all non-matching rows (full outer join)

outerjoin_Trans_users=pd.merge(left=transactions, right=users,how='outer',on='UserID',indicator=True)

# 16. Determine which sessions occurred on the same day each user registered

users_sessions=pd.merge(left=users, right=sessions,how='inner',on='UserID',indicator=True)
same_sessions_regoccur=users_sessions[users_sessions['Registered']==users_sessions['SessionDate']]

# 17. Build a dataset with every possible (UserID, ProductID) pair (cross join)

users['key'] = 1
products['key'] = 1
users_products_join=pd.merge(users, products, on='key').loc[:, ('UserID','ProductID')]

# 18. Determine how much quantity of each product was purchased by each user

join_product_transactions=pd.merge(transactions,products,on='ProductID').loc[:,('UserID','ProductID','Product','Quantity')]

user_products_data=pd.merge(users,join_product_transactions,on='UserID').loc[:,('User','Product','Quantity')]

users_products_aggregate=pd.pivot_table(user_products_data,values='Quantity',index='User',columns='Product',aggfunc='sum')





