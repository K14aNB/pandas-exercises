# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3
#     name: python3
# ---

# %% [markdown]
# # **Filtering and Sorting - Chipotle**

# %% [markdown]
# **Import the libraries**

# %%
import pandas as pd
import os
import sys
from urllib3 import PoolManager,request

# %% [markdown]
# **Environment Setup**

# %%
# Setup Environment
# Github gist url for Python Script which will perform environment setup
env_url = 'https://gist.githubusercontent.com/K14aNB/46becb626d36ad8fa8d445616241dfef/raw/'
http = PoolManager()
response = http.request('GET',env_url)
if response.status==200:
    exec(response.data.decode('utf-8'))
    setup(repo_path='pandas-exercises',nb_name='Filtering-and-Sorting-Chipotle')

# %% [markdown]
# **Read the data**

# %%
if 'google.colab' not in sys.modules:
    dir=os.path.join(os.getcwd(),'Data Science','Git Repos','pandas-exercises')
else:
    dir=os.getcwd()
chipo=pd.read_csv(os.path.join(dir,'data','chipotle.tsv'),sep='\t')

# %%
chipo.head()

# %%
chipo.info()

# %% [markdown]
# **How many products cost more than $10.00?**

# %%
# Converting item price column to float64
chipo['item_price'] = chipo['item_price'].map(lambda x:x.split('$')[1])
chipo['item_price'] = chipo['item_price'].astype('float64')

# %%
# Total Number of items that cost more than 10.00
chipo.loc[chipo['item_price']>10.00,'item_name'].count()

# %%
# Number of unique products that cost more than 10.00
chipo.loc[chipo['item_price']>10.00,'item_name'].nunique()

# %% [markdown]
# **What is the price of each item?**

# %%
chipo.loc[:,['item_name','item_price']]

# %% [markdown]
# **Sort by name of the item**

# %%
chipo.sort_values(by='item_name')

# %% [markdown]
# **What is the quantity of most expensive item ordered?**

# %%
chipo.loc[chipo['item_price']==chipo['item_price'].max(),'quantity'].values[0]

# %% [markdown]
# **How many times a Veggie Salad Bowl was ordered?**

# %%
chipo['item_name'].value_counts()['Veggie Salad Bowl']

# %% [markdown]
# **How many times did someone order more than one Canned Soda?**

# %%
chipo.loc[(chipo['item_name']=='Canned Soda')&(chipo['quantity']>1),'item_name'].count()

# %%
