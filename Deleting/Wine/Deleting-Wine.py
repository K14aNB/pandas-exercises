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
# # **Deleting - Wine**

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
import numpy as np
import pandas as pd
import os
import env_setup

# %% [markdown]
# **Environment Setup**

# %%
# Setup Environment(Downloading data and setting output formats specified in config.yaml)
result_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Deleting-Wine')

# %% [markdown]
# **Read the data**

# %%
wine=pd.read_csv(os.path.join(result_path,'wine.data'))

# %%
wine.head()

# %%
wine.info()

# %% [markdown]
# **Delete the first,fourth,seventh,nineth,eleventh,thirteenth and fourteenth columns**

# %%
wine=wine.drop(columns=['1','2.43','2.8','.28','5.64','3.92','1065'],axis=1)

# %%
wine.head()

# %% [markdown]
# **Rename the columns**

# %%
wine=wine.rename(columns={'14.23':'alcohol','1.71':'malic_acid','15.6':'alcalinity_of_ash','127':'magnesium','3.06':'flavenoids','2.29':'proanthocyanins','1.04':'hue'})

# %%
wine.head()

# %% [markdown]
# **Set the first 3 rows from `alcohol` as NaN**

# %%
wine.loc[:2,'alcohol']=np.NaN

# %%
wine.head()

# %% [markdown]
# **Set the values of row 3 and 4 of `magnesium` as NaN**

# %%
wine.loc[2:3,'magnesium']=np.NaN

# %%
wine.head()

# %% [markdown]
# **Fill the value of NaN with 10 in `alcohol` and 100 in `magnesium`**

# %%
wine['alcohol']=wine['alcohol'].replace(to_replace=np.NaN,value=10)
wine['magnesium']=wine['magnesium'].replace(to_replace=np.NaN,value=100)
wine.head()

# %% [markdown]
# **Count the number of missing values**

# %%
wine.isna().sum().sum()

# %% [markdown]
# **Create an array of 10 random numbers up until 10**

# %%
arr=np.linspace(0,10,10,dtype='int64')

# %%
arr

# %% [markdown]
# **Assign NaN as value by using random numbers generated as index**

# %%
wine.loc[arr,:]=np.NaN

# %%
wine.head(15)

# %% [markdown]
# **How many missing values do we have?**

# %%
wine.isna().sum().sum()

# %% [markdown]
# **Delete the rows containing missing values**

# %%
wine=wine.dropna()

# %%
wine.head(15)

# %% [markdown]
# **Reset the index**

# %%
wine=wine.reset_index(drop=True)

# %%
wine.head(15)

# %%
