#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing packages
import numpy as np
import pandas as pd

# opening dataframe file from local computer
df1 = pd.read_csv(r'G:\Python projects\suicide rates\master.csv')

# cleaning up data removing columns
df1 = df1.drop(columns = ['country-year', 'HDI for year', 'gdp_per_capita ($)', 'generation'])

# sorting data frame
df1 = df1.sort_values(by=['sex', 'year', "country", "age"], ascending=True)

# resetting index
df1 = df1.reset_index(drop = True)

# dropping one column
df1 = df1.iloc[: , :-1]
df1


# In[ ]:




