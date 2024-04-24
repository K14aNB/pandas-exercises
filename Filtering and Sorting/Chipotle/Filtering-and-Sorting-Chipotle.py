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
# **Check and install the dependencies**

# %%
# !curl -sSL 'https://raw.githubusercontent.com/K14aNB/pandas-exercises/main/requirements.txt'

# %%
# Run this command in terminal before running this notebook as .py script
# Installs dependencies from requirements.txt present in the repo
# %%capture
# !pip install -r 'https://raw.githubusercontent.com/K14aNB/pandas-exercises/main/requirements.txt'

# %% [markdown]
# **Import the libraries**

# %%
import pandas as pd
import os
import env_setup

# %% [markdown]
# **Environment Setup**

# %%
# Setup Environment(Downloading data and setting output formats specified in config.yaml)
result_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Filtering-and-Sorting-Chipotle')

# %% [markdown]
# **Read the data**

# %%
chipo=pd.read_csv(os.path.join(result_path,'chipotle.tsv'),sep='\t')

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
