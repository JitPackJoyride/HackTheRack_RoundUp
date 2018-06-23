
# coding: utf-8

# In[1]:


import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

df = pd.read_csv('df_transactions_clean.csv')


# In[2]:


basket = (df.head(500000)
          .groupby(['Trans ID', 'Prod Name (Chi)'])['Sold Qty']
          .sum().unstack().reset_index().fillna(0)
          .set_index('Trans ID'))
basket.astype(int)


# In[4]:


def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

basket_sets = basket.applymap(encode_units)


# In[25]:


frequent_itemsets = apriori(basket_sets, min_support=0.002, use_colnames=True) 
#should be a support of 0.7 hopefully but there are too much octopus recharges that other data have a lower percentage of total amount


# In[34]:


rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules
# use the rules table to come up with conclusions

