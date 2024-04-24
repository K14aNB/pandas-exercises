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
# # **Visualization - Chipotle**

# %% [markdown]
# **Check and install dependencies**

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
import matplotlib.pyplot as plt
import seaborn as sns
import env_setup
import os

# %% [markdown]
# **Environment Setup**

# %%
# Setup Environment(Downloading data and setting output formats specified in config.yaml)
result_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Visualization-Chipotle')

# %% [markdown]
# **Read the data**

# %%
chipo=pd.read_csv(os.path.join(result_path,'chipotle.tsv'),sep='\t')

# %%
chipo.head()

# %%
chipo.info()

# %% [markdown]
# **First 10 entries**

# %%
chipo.head(10)

# %% [markdown]
# **Histogram of top 5 items bought**

# %%
top_5_items=chipo['item_name'].value_counts().nlargest(5)

# %%
# Histogram for Top 5 items bought
fig=plt.figure(figsize=(10,5))
sns.barplot(x=top_5_items.index,y=top_5_items.values)
plt.show()

# %% [markdown]
# **Create a scatter plot with number of items ordered per order price**

# %%
# Convert item_price and order_price into float
chipo['item_price']=chipo['item_price'].map(lambda x:x.split('$')[1].strip()).astype('float64')

# %%
# Order price column
chipo['order_price']=chipo['item_price']*chipo['quantity']

# %%
orders=chipo.groupby('order_id')[['order_price','quantity']].sum()

# %%
orders

# %%
# Scatter plot for number of items ordered per order price
sns.scatterplot(x='order_price',y='quantity',data=orders)
plt.show()

# %%
