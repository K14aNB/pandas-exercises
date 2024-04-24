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
# **Check and install the dependencies**

# %%
# !curl -sSL "https://raw.githubusercontent.com/K14aNB/pandas-exercises/main/requirements.txt"

# %%
# Run this command in terminal before running this notebook as .py script
# Installs dependencies from requirements.txt present in the repo
# %%capture
# !pip install -r "https://raw.githubusercontent.com/K14aNB/pandas-exercises/main/requirements.txt"

# %% [markdown]
# **Import the libraries**

# %%
import pandas as pd
import os
import env_setup

# %% [markdown]
# **Environment setup**

# %%
# Setup Environment(Downloading data and setting output formats specified in config.yaml)
results_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Getting-to-know-the-data-Chipotle')

# %% [markdown]
# **Read the data**

# %%
chipo = pd.read_csv(os.path.join(results_path,'chipotle.tsv'),sep='\t')

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
# **Most Ordered Item in `choice_description` column**

# %%
# Most ordered item in the choice_description column
chipo['choice_description'].value_counts().index[0]

# %% [markdown]
# **How many items were ordered in total**

# %%
# How many items were ordered in total
chipo['quantity'].sum()

# %% [markdown]
# **Change dtype of `item_price` to float**

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
