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
# # **Visualization - Online Retail**

# %% [markdown]
# **Check and install the dependencies**

# %%
# !curl -sSL https://raw.githubusercontent.com/K14aNB/pandas-exercises/main/requirements.txt

# %%
# Run this command in terminal before running this notebook as .py script
# Installs dependencies from requirements.txt present in the repo
# %%capture
# !pip install -r https://raw.githubusercontent.com/K14aNB/pandas-exercises/main/requirements.txt

# %% [markdown]
# **Import the libraries**

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import env_setup

# %% [markdown]
# **Environment Setup**

# %%
# Setup Environment(Downloading data and setting output formats specified in config.yaml)
result_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Visualization-Online-Retail')

# %% [markdown]
# **Read the data**

# %%
online_rt=pd.read_csv(os.path.join(result_path,'Online_Retail.csv'),encoding='latin_1')

# %%
online_rt.head()

# %%
online_rt.info()

# %% [markdown]
# **Create a Histogram with the 10 countries that have most quantity ordered except UK**

# %%
# Group by Countries with Quantity
quantity_by_countries=online_rt.groupby('Country')['Quantity'].agg('count')

# %%
# Filtering Top 10 countries with most order quantity
top_10_most_order_quantity=quantity_by_countries.sort_values(ascending=False).head(10)

# %%
# Excluding United Kingdom from results
top_10_most_order_quantity_except_uk=top_10_most_order_quantity[1:]

# %%
# Plot bar graph
fig = plt.figure(figsize=(10,5))
sns.barplot(top_10_most_order_quantity_except_uk)
plt.show()

# %% [markdown]
# **Exclude negative Quantities**

# %%
positive_quants=online_rt.loc[online_rt['Quantity']>0]

# %%
positive_quants

# %% [markdown]
# **Create a scatterplot with `Quantity` per `UnitPrice` by `CustomerID` for top 3 Countries except United Kingdom**

# %%
positive_quants.loc[:,'Revenue']=positive_quants['Quantity']*positive_quants['UnitPrice']

# %%
grouped_countries=positive_quants.groupby('Country')['Revenue'].agg('sum').sort_values(ascending=False)

# %%
top_3_countries=grouped_countries[1:4].index.to_list()

# %%
top_3_countries

# %%
group=positive_quants.loc[positive_quants['Country'].isin(top_3_countries)].groupby(['CustomerID','Country'])['Revenue'].agg('sum')

# %%
fig=plt.figure(group.loc[('Germany'),:])

# %%
group

# %%
