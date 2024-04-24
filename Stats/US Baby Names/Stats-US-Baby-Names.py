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
# # **US - Baby Names**

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
import env_setup
import os

# %% [markdown]
# **Environment Setup**

# %%
# Setup environment(Downloading data and setting output formats specified in config.yaml)
result_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Stats-US-Baby-Names')

# %% [markdown]
# **Read the data**

# %%
baby_names=pd.read_csv(os.path.join(result_path,'US_Baby_Names_right.csv'))

# %%
baby_names.head()

# %%
baby_names.info()

# %% [markdown]
# **First 10 entries**

# %%
baby_names.head(10)

# %% [markdown]
# **Delete the column `Unamed: 0` and `Id`**

# %%
baby_names=baby_names.drop(columns=['Unnamed: 0','Id'])
baby_names

# %% [markdown]
# **Is there more male or female names in the dataset?**

# %%
baby_names.groupby('Gender')['Name'].agg('count')

# %% [markdown]
# **Group the dataset by `Name` and assign to `names`**

# %%
names=baby_names.groupby('Name')['Count'].sum()
names

# %% [markdown]
# **How many different names exist in the dataset?**

# %%
baby_names['Name'].nunique()

# %% [markdown]
# **What is the `Name` with most occurances?**

# %%
baby_names['Name'].value_counts().idxmax()

# %% [markdown]
# **How many different `Names` have the least occurrences?**

# %%
# TO DO

# %% [markdown]
# **What is the median of `Name` occurrence?**

# %%
baby_names['Count'].median()

# %%
baby_names.loc[baby_names['Count']==baby_names['Count'].median(),'Name']

# %% [markdown]
# **What is the standard deviation of names?**

# %%
baby_names['Count'].std()

# %% [markdown]
# **Summary**

# %%
baby_names['Count'].describe()

# %%
