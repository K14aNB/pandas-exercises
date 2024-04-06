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
# # **Getting to know the Data - Chipotle**

# %% [markdown]
# **Import the libraries**

# %%
import pandas as pd
import os
import sys
from urllib3 import PoolManager,request

# %% [markdown]
# **Environment setup**

# %%
# Setup Environment
# Github gist URL for Python script which will perform environment setup
env_url = 'https://gist.githubusercontent.com/K14aNB/46becb626d36ad8fa8d445616241dfef/raw/'
http = PoolManager()
setup_env_response = http.request('GET',env_url)
if setup_env_response.status==200:
    exec(setup_env_response.data.decode('utf-8'))
    setup(repo_path='pandas-exercises',nb_name='Chipotle')

# %% [markdown]
# **Read the data**

# %%
if 'google.colab' not in sys.modules:
    dir=os.path.join(os.getcwd(),'Data Science','Git Repos','pandas-exercises')
else:
    dir=os.getcwd()
chipo = pd.read_csv(os.path.join(dir,'data','chipotle.tsv'),sep='\t')

# %%
chipo.head(10)

# %%
chipo.info()

# %% [markdown]
# **Number of rows and columns in the DataFrame**

# %%
chipo.shape

# %% [markdown]
# **Column names**

# %%
chipo.columns

# %% [markdown]
# **Index of the DataFrame**

# %%
chipo.index

# %% [markdown]
# **Most Ordered Item name**

# %%
# Most Ordered item
chipo['item_name'].value_counts().index[0]

# %% [markdown]
# **Quantity of Most Ordered Item**

# %%
# Quantity for most ordered item
chipo.loc[chipo['item_name']==chipo['item_name'].value_counts().index[0],'quantity'].sum()

# %% [markdown]
# **Most Ordered Item in choice_description column**

# %%
# Most ordered item in the choice_description column
chipo['choice_description'].value_counts().index[0]

# %% [markdown]
# **How many items were ordered in total**

# %%
# How many items were ordered in total
chipo['quantity'].sum()

# %% [markdown]
# **Change dtype of price to float**

# %%
chipo['item_price'].dtypes

# %%
chipo['item_price']=chipo['item_price'].map(lambda x:x.split('$')[1])

# %%
chipo['item_price'] = chipo['item_price'].astype('float64')

# %%
chipo['item_price']

# %% [markdown]
# **Total Revenue**

# %%
# Total Revenue
revenue = chipo['quantity']*chipo['item_price']
revenue = revenue.sum()
print(revenue)

# %% [markdown]
# **How many orders were made?**

# %%
# Number of orders
chipo['order_id'].nunique()

# %% [markdown]
# **Average revenue per order**

# %%
# Average revenue per order
chipo['revenue'] = chipo['quantity']*chipo['item_price']
chipo.groupby('order_id')['revenue'].agg('mean')

# %% [markdown]
# **How many different items are sold**

# %%
# Number of unique items sold
chipo['item_name'].nunique()

# %%
