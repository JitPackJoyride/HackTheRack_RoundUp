
# coding: utf-8

# In[97]:


import pandas as pd
import numpy as np
import datetime
df_transactions = pd.read_csv('transactions.csv')


# In[100]:


###################update date format###################
date_format = '%Y-%m-%d'

df_transactions['Date'] = pd.to_datetime(df_transactions['Date'],format=date_format)
 #check max txn date
max_date = df_transactions['Date'].max()
d = datetime.timedelta(1)
today = max_date + d

#df_transactions['Member ID'] = df_transactions['Member ID'].astype(str)
#df_transactions['Trans ID'] = df_transactions['Trans ID'].astype(str)

###################data preview###################
# df_transactions.head()


# In[101]:


#print(df_transactions.describe())  #-ve field: Sold Qty, Amount
#print(df_transactions.info())
#print(df_transactions.shape)  #(2759843, 16)


# In[102]:


#drop duplicate (2622316, 16)
df_transactions.drop_duplicates(keep='first', inplace=True) 


# In[105]:


#replace member id with trans id if null

df_transactions['Member ID'] = np.where(df_transactions['Member ID'].isnull(),df_transactions['Trans ID'],df_transactions['Member ID']) 


# In[106]:


df_transactions['Member ID'] = df_transactions['Member ID'].astype('int64')


# In[107]:


#select +ve price only
df_pos = df_transactions[(df_transactions['Sold Qty'] > 0) & (df_transactions['Amount'] > 0)]
print(df_pos.shape) #(2077101, 16)
print(df_pos.isnull().sum())  #783 is null for Subcat


# In[108]:


#a = df_pos[df_pos['Subcat'].isnull()]
#a['Prod Name (Chi)'].unique()

df_pos.loc[(df_pos['Prod Name (Chi)'] == 'Ã§ÂÂÃ©ÂÂÃ¥Â°ÂÃ¦Â¥Â­Ã©Â¦ÂÃ¥ÂÂ£Ã§ÂÂ 8Ã§Â²ÂÃ¨Â£Â')&(df_pos['Subcat'].isnull()), 'Subcat']= 'Gum'


# In[109]:


df_pos.head()


# In[119]:


df_pos.to_csv('df_transactions_clean.csv',index=False, encoding='utf-8')

