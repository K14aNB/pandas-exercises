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
# Github gist url for Python script which will perform environment setup
env_url='https://gist.githubusercontent.com/K14aNB/46becb626d36ad8fa8d445616241dfef/raw/'
http=PoolManager()
setup_env_response=http.request('GET',env_url)
if setup_env_response.status==200:
    exec(setup_env_response.data.decode('utf-8'))
    setup(repo_path='pandas-exercises',nb_name='Occupation')

# %% [markdown]
# **Read the data**

# %%
if 'google.colab' not in sys.modules:
    dir=os.path.join(os.getcwd(),'Data Science','Git Repos','pandas-exercises')
else:
    dir='/content'
users=pd.read_csv(os.path.join(dir,'data','u.user'),sep='|',index_col='user_id')

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
# **Print only the occupation column**

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
# **Summarize only occupation column**

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
