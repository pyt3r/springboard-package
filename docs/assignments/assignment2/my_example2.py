"""
my_example2.py
==========================

Here is a plot example
"""


#%%
# ## Lets create some data
# pandas dataframes have a html representation, and this is captured:

import pandas as pd

df = pd.DataFrame({'col1': [10,20,30],
                   'col2': [40,50,60]})
print( df )
#%%
# ## Lets plot the data

ax = df.plot(x='col1', y='col2', kind='line', title='col1 vs col2')

# %%
