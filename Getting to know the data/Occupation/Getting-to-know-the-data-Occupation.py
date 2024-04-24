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
# # **Getting to know the Data - Occupation**

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
results_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Getting-to-know-the-data-Occupation')

# %% [markdown]
# **Read the data**

# %%
users=pd.read_csv(os.path.join(results_path,'u.user'),sep='|',index_col='user_id')

# %%
users.head()

# %%
users.info()

# %% [markdown]
# **First 25 entries**

# %%
users.head(25)

# %% [markdown]
# **Last 10 entries**

# %%
users.tail(10)

# %% [markdown]
# **Number of Observations**

# %%
users.shape[0]

# %% [markdown]
# **Number of columns**

# %%
users.shape[1]

# %% [markdown]
# **Print column names**

# %%
users.columns.to_list()

# %% [markdown]
# **Index of the dataset**

# %%
users.index

# %% [markdown]
# **Data type of each column**

# %%
users.dtypes

# %% [markdown]
# **Print only the `occupation` column**

# %%
users['occupation']

# %% [markdown]
# **Different occupations in the dataset**

# %%
users['occupation'].value_counts().index.to_list()

# %% [markdown]
# **Most Frequent Occupation**

# %%
users['occupation'].mode()[0]

# %% [markdown]
# **Summarize the DataFrame**

# %%
users.describe().T

# %% [markdown]
# **Summarize all columns**

# %%
users.describe(include='O').T

# %% [markdown]
# **Summarize only `occupation` column**

# %%
users['occupation'].describe(include='O')

# %% [markdown]
# **Mean age of users**

# %%
round(users['age'].mean(),2)

# %% [markdown]
# **What is the age with least occurence**

# %%
users['age'].value_counts().index[-1]

# %%
